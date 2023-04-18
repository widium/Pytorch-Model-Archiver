## Pytorch-Model-Archiver
Export and Import custom Pytorch Module in another python environment like `model.save()` of tensorflow

### Package Structure
~~~bash
archive
├── __init__.py
├── __pycache__
├── loading.py
├── saving.py
└── utils
~~~

### Usage
![](https://i.imgur.com/msua3dJ.png)
#### Saving
- example here [saving.ipynb](/saving.ipynb)
~~~python
from archive.saving import save_module

save_module(
    module_instance=model, 
    model_name="model_test",
    source_code_files=["efficientnetv1.py", "frozen.py"] # The first path must be the class definition
)
~~~
- Output Log
~~~text
[INFO] : Create [model_test] directory
[INFO] : Source file [efficientnetv1.py] saved Successfuly here : [model_test/efficientnetv1.py]
[INFO] : The main class source code is [model_test/efficientnetv1.py]
[INFO] : Source file [frozen.py] saved Successfuly here : [model_test/frozen.py]
[WARNING] : Skipping saving non-serializable attribute : [T_destination]
[INFO] : Saving [5,292,391] Parameters in [model_test/module_data.pth]
[INFO] : Saving [15] Attributes of [EfficientNetFoodClassifier] in [model_test/module_data.pth]
[INFO] : Entire Custom Module Saved Successfully in [model_test]
~~~
> This Message : `[WARNING] : Skipping saving non-serializable attribute : [T_destination]` Meaning we can't serialized `T_destination` attribute because he track the device (CPU or GPU) where a tensor should be moved when calling the `to()` method of `Module` class. 
~~~bash
model_test
├── efficientnetv1.py
└── module_data.pth

1 directory, 2 files
~~~
### Loading with same format 
- example here [loading.ipynb](/loading.ipynb)
~~~bash
model_test
├── efficientnetv1.py
└── module_data.pth

1 directory, 2 files
~~~
~~~python
from archive.loading import load_module

model = load_module(module_path="model_test")
~~~
- Output log
~~~text
[INFO] : find model directory [model_test]
[INFO] : find module data file [model_test/module_data.pth]
[INFO] : find source code of [EfficientNetFoodClassifier] in [model_test/efficientnetv1.py]
[INFO] : Reconstruct the Class Object [EfficientNetFoodClassifier]
[INFO] : Insert [5,292,391] Parameters inside [EfficientNetFoodClassifier]
[INFO] : Reconstruct Model Object Successfully !
~~~

