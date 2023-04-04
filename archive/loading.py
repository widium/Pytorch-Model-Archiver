# *************************************************************************** #
#                                                                              #
#    loading.py                                                                #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/04/04 10:32:34 by Widium                                    #
#    Updated: 2023/04/04 10:32:34 by Widium                                    #
#                                                                              #
# **************************************************************************** #

from typing import Any

import torch
from torch.nn import Module

from pathlib import Path

from .utils.dir_file_ops import python_file_to_module

from .utils.module_utils import count_parameters

from .utils.instance_inspector import update_instance_attribute

# **************************************************************************** #
 
def load_module(module_path: str) -> Module:
    """
    load Custom Pytorch Module Instance with saved Attribute and Parameters

    Args:
        module_path (str): dir path of saved module

    Raises:
        FileExistsError: Check if Directory exist
        FileExistsError: Check if Serialized instance data file exist
        FileExistsError: Check if Python instance source code file exist

    Returns:
        Module: instance reconstructed 
    """
    module_path = Path(module_path)
    module_data_file = module_path / f"module_data.pth"
    
    ## ----------------------------- Check Directory and Serialized File ----------------------------- ## 
    
    if not module_path.is_dir():
        raise FileExistsError(f"[ERROR] : {module_path} does not exist")
    else:
        print(f"[INFO] : find model directory [{module_path}]")
        
    if not module_data_file.is_file():
        raise FileExistsError(f"[ERROR] : {module_data_file} does not exist")
    else :
        print(f"[INFO] : find module data file [{module_data_file}]")
    
    ## ----------------------------- Load all Module Instance Data ----------------------------- ## 
    
    module_data = torch.load(f=module_data_file)
        
    class_name = module_data["class_name"]
    class_arguments = module_data["class_constructor_arguments"]
    attributes_value = module_data["attributes_value"]
    module_parameters = module_data["parameters"]
    source_code_path = module_data["source_code_path"]

    if not Path(source_code_path).is_file():
        raise FileExistsError(f"[ERROR] : {source_code_path} does not exist")
    else:
        print(f"[INFO] : find source code of [{class_name}] in [{source_code_path}]")
    
    ## ----------------------------- Reconstruct the Module Instance ----------------------------- ## 
    
    module = python_file_to_module(
        file_path=source_code_path,
        base_path=""
    )
    
    print(f"[INFO] : Reconstruct the Class Object [{class_name}]")
    class_constructor = getattr(module, class_name)
    model_instance = class_constructor(**class_arguments)
    
    model_instance = update_instance_attribute(
        instance=model_instance,
        new_attribute=attributes_value
    )
    print(f"[INFO] : Insert [{count_parameters(model_instance):,}] Parameters inside [{class_name}]")
    model_instance.load_state_dict(module_parameters)
    
    print(f"[INFO] : Reconstruct Model Object Successfully !")

    return (model_instance)