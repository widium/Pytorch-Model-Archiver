# *************************************************************************** #
#                                                                              #
#    dir_file_ops.py                                                           #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/04/04 16:26:51 by Widium                                    #
#    Updated: 2023/04/04 16:26:51 by Widium                                    #
#                                                                              #
# **************************************************************************** #

from typing import Any

from importlib import import_module
from pathlib import Path

# **************************************************************************** #

def create_directory(dir_path : str = "new_dir")->Path:
    """
    Create a Directory in Specified Locations

    Args:
        dir_path (str, optional): dir name and location path/to/my/new_dir. Defaults to "new_dir".

    Raises:
        FileExistsError: Error raise when the directory exist 

    Returns:
        Path: output pathlib Path of new directory
    """
    dir_path = Path(dir_path)
    
    # If the folder exist don't create it
    if dir_path.is_dir():
        raise FileExistsError(f"[ERROR] : {dir_path} directory exists. do nothing")
    
    else:
        print(f"[INFO] : Create [{dir_path}] directory")
        dir_path.mkdir(parents=True, exist_ok=True)
    
    return (dir_path)

# **************************************************************************** #

def duplicate_file_to_destination(
    source: str, 
    destination: str
) -> Path:
    """
    Duplicate File Content and Name Into another path 

    Args:
        `source` (str): path of file to duplicate
        `destination` (str): destination of duplicate file

    Raises:
        FileExistsError: Give an Error if the file already exist in destination

    Returns:
        `Path`: Output pathlib Path of duplicate File
    """
    source_path = Path(source)
    new_file_path = Path(destination)

    # If the destination is a directory, append the source file name to the destination
    if new_file_path.is_dir():
        new_file_path = new_file_path / source_path.name

    if new_file_path.exists():
        raise FileExistsError(f"File [{new_file_path}] already exists Here.")
    else :
        new_file_path.touch()
        
    # extract content of source file
    file_content = source_path.read_bytes()
    
    # write content into new file
    new_file_path.write_bytes(file_content)

    print(f"[INFO] : Source file [{source_path}] saved Successfuly here : [{new_file_path}]")
    return (new_file_path)

# **************************************************************************** #

def python_file_to_module(
    file_path : str, 
    base_path : str = ""
)->Any:
    """Convert Python File path into Module to Import 

    Args:
        `file_path` (str): file path of python file into directory
        `base_path` (str, optional): base path of python module name we want for generalized in other environnement. Defaults to "".

    Returns:
        Any: return module class of python file
    """
    module_path = Path(file_path).relative_to(base_path)
    module_name = str(module_path).replace(".py", "").replace("/", ".")
    module = import_module(name=module_name)
    return (module)
