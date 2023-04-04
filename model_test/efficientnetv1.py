from torch.nn import Module
from torch.nn import Sequential
from torch.nn import Dropout, Linear, Flatten
from torch import Tensor

from torchinfo import summary
from torchvision.models import EfficientNet_B0_Weights
from torchvision.models import efficientnet_b0

def frozen_module_parameters(module : Module)->Module:
    """Frozen all Module parameters

    Args:
        module (Module): Module

    Returns:
        Module: New Module with all requires_grad = False
    """
    for parameter in module.parameters():
        parameter.requires_grad = False
    
    return (module)

# Get the Weight of Model `DEFAULT` == last best version
weights = EfficientNet_B0_Weights.DEFAULT

# Give Weight to model architecture
efficientnetb0 = efficientnet_b0(weights=weights)

class EfficientNetFoodClassifier(Module):
    
    def __init__(self, nbr_classes : int):
        super().__init__()
        
        self.efficientnet = efficientnetb0
        self.nbr_classes = nbr_classes
        
        self.features_extractor = frozen_module_parameters(module=efficientnetb0.features)
        
        self.features_vector = efficientnetb0.avgpool
        
        self.flatten = Flatten()
        
        self.classifier = Sequential(
                            Dropout(p=0.2),
                            Linear(in_features=1280, out_features=nbr_classes)
                        )
    
    def forward(self, x : Tensor):
        
        x = self.features_extractor(x)
        x = self.features_vector(x)
        x = self.flatten(x)
        x = self.classifier(x)
        
        return (x)
