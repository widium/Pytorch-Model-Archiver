# *************************************************************************** #
#                                                                              #
#    exporting.py                                                              #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/04/04 10:32:31 by Widium                                    #
#    Updated: 2023/04/04 10:32:31 by Widium                                    #
#                                                                              #
# **************************************************************************** #

import torch
from torch.nn import Module

from pathlib import Path

from .utils.dir_file_ops import create_directory
from .utils.dir_file_ops import duplicate_file_to_destination

from .utils.instance_inspector import get_instance_attributes_value
from .utils.instance_inspector import get_instance_constructor_args

from .utils.module_utils import count_parameters

# **************************************************************************** #   
    
def save_module(
    module_instance : Module,
    model_name : str,
    class_source_code_file_path : str,
    saved_path : str = "."
)->None:
    """
    Saving Pytorch Module in directory with 
    * his class source code file
    * his constructor's arguments
    * his attributes values
    * his entire parameters (Module.state_dict())
    all of this allow to reconstruct the same Module instance later

    Args:
        module_instance (Module): custom Pytorch module instance
        model_name (str): name of saved directory
        class_source_code_file_path (str): python file with class definition
        saved_path (str, optional): path to create the directory. Defaults to ".".
    """
    module_directory = Path(saved_path) / model_name
    module_instance_file = module_directory / f"module_data.pth"
    
    create_directory(dir_path=module_directory)
    
    # Duplicate the source code file into archive directory
    class_source_code_path = duplicate_file_to_destination(
                source=class_source_code_file_path,
                destination=module_directory
    )
    
    ## ---------------------- Get and Store the instance data ---------------------- ##
    
    class_name = module_instance.__class__.__name__
    constructor_arguments = get_instance_constructor_args(instance=module_instance)
    attributes_value = get_instance_attributes_value(instance=module_instance)
    
    module_instance_data = {
        "class_name" : class_name,
        "source_code_path" : str(class_source_code_path),
        "class_constructor_arguments" : constructor_arguments,
        "attributes_value" : attributes_value,
        "parameters" : module_instance.state_dict()
    }
    
    ## ---------------------- Save all instance data in serialized Dictionary ---------------------- ##
    
    torch.save(
        obj=module_instance_data,
        f=module_instance_file
    )
    
    print(f"[INFO] : Saving [{count_parameters(module_instance):,}] Parameters in [{module_instance_file}]")
    print(f"[INFO] : Saving [{len(attributes_value)}] Attributes of [{class_name}] in [{module_instance_file}]")
    print(f"[INFO] : Entire Custom Module Saved Successfully in [{module_directory}]")