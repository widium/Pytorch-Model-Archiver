# *************************************************************************** #
#                                                                              #
#    efficientnetv1.py                                                         #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/04/04 16:55:46 by Widium                                    #
#    Updated: 2023/04/04 16:55:46 by Widium                                    #
#                                                                              #
# **************************************************************************** #

from torch.nn import Module
from torch.nn import Sequential
from torch.nn import Dropout, Linear, Flatten
from torch import Tensor

from torchvision.models import EfficientNet_B0_Weights
from torchvision.models import efficientnet_b0

from frozen import frozen_module_parameters

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
