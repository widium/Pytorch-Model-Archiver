# *************************************************************************** #
#                                                                              #
#    module_utils.py                                                           #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/04/04 16:34:11 by Widium                                    #
#    Updated: 2023/04/04 16:34:11 by Widium                                    #
#                                                                              #
# **************************************************************************** #

from torch.nn import Module

# **************************************************************************** #

def count_parameters(model : Module)->int:
    """
    Count Number of Parameters in Pytorch Module

    Args:
        model (Module): instance of Pytorch Module

    Returns:
        int: number of parameters
    """
    parameters_per_tensor = [param.numel() for param in model.parameters()]
    nbr_parameters = sum(parameters_per_tensor)
    return (nbr_parameters)