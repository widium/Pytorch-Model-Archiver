# *************************************************************************** #
#                                                                              #
#    frozen.py                                                                 #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/04/18 17:34:30 by Widium                                    #
#    Updated: 2023/04/18 17:34:30 by Widium                                    #
#                                                                              #
# **************************************************************************** #

from torch.nn import Module

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