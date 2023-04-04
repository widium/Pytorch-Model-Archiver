# *************************************************************************** #
#                                                                              #
#    instance_inspector.py                                                     #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/04/04 16:32:52 by Widium                                    #
#    Updated: 2023/04/04 16:32:52 by Widium                                    #
#                                                                              #
# **************************************************************************** #

from typing import Any, Dict

import inspect
import pickle

# **************************************************************************** #

def get_instance_constructor_args(instance : Any)->Dict:
        """recover the constructor arguments value of instance in dictionary

        Args:
            class_instance (any): instance of any class

        Returns:
            dict: dictionary of instance arguments
        """
        constructor_method = instance.__class__.__init__
        constructor_arguments = inspect.signature(constructor_method)
        constructor_parameters = constructor_arguments.parameters
        
        constructor_parameter_values = dict()
        
        for name in constructor_parameters:
            if name == 'self':
                continue
                
            constructor_parameter_values[name] = getattr(instance, name)
        
        return (constructor_parameter_values)

# **************************************************************************** #

def is_serializable(object : Any)->bool:
    """
    Check if an object is Serializable with Pickle

    Args:
        object (Any): Object want to serialized

    Returns:
        bool: True of False
    """
    try:
        pickle.dumps(object)
        return True

    except (TypeError, pickle.PicklingError):
        return False
    
# **************************************************************************** #

def get_instance_attributes_value(instance):
    """Extract all the variable value of an instance in Dictionary

    Args:
        instance (Any): instance of Any Class

    Returns:
        dict: dictionary of instance variables value
    """
    instance_attributes_value = dict()
    
    for attribute in dir(instance):
        
        attribute_value = getattr(instance, attribute)
        
        # if is method attribute or special or private attributes.
        if callable(attribute_value) or attribute.startswith("__"):
            continue
        else:
            if is_serializable(object=attribute_value):
                instance_attributes_value[attribute] = attribute_value
            else :
                print(f"[WARNING] : Skipping saving non-serializable attribute : [{attribute}]")
        
    return (instance_attributes_value)

# **************************************************************************** #

def update_instance_attribute(instance : Any, new_attribute : dict)->Any:
    """Update and give new Attribute an Instance 

    Args:
        instance (Any): instance of any class
        new_attribute (dict): dictionary "attribute_name" : attribute_value

    Returns:
        Any: instance updated
    """
    # Update the instance with its attributes
    for attribute, value in new_attribute.items():
        setattr(instance, attribute, value)
    
    return (instance)    