
# CogForge 🛠️

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

**CogForge** is a lightweight, local-module handler designed for Python developers. It allows you to seamlessly code or import standalone codes or modules, turning them into a structured local module management system. Built with security and error handling at its core, **CogForge** aims to minimize code-breaking errors through an innovative error code system, ensuring your development process is as smooth and efficient as possible.

## Features 🌟

- **Local Module Management**: Organize your Python codes and modules locally with an easy-to-use interface.
- **Error Handling System**: Advanced error code system to help you quickly identify and resolve issues.
- **Security First**: Designed with security in mind to protect your code during the module handling process.
- **Simplicity**: Intuitive design for easy adoption and minimal learning curve.
- **Efficiency**: Minimizes code-breaking errors, enhancing your coding efficiency.

## Installation 💾

```bash
pip install cogforge
```

## Quick Start 🚀

1. **Create a new module**:

   ```python
   from cogforge import Forge

   my_module = Forge(name="MyModule")
   ```

2. **Add code or import a module**:

   ```python
   my_module.add_code("def hello_world():\\n    print('Hello, World!')")
   ```

   or

   ```python
   my_module.import_module('path/to/your/module')
   ```

3. **Compile your module**:

   ```python
   my_module.compile()
   ```

4. **Enjoy your structured local module**! 🎉

## Usage Example

### Source Code

```python
import os
import importlib.util

def getAllCogs(path):
    return [cog for cog in os.listdir(path) if cog.endswith('.py')]

class CogsOSError(Exception):
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code
    
    def __str__(self):
        if self.error_code:
            return f"{super().__str__()} [Error Code: {self.error_code}]"
        return super().__str__()
    
def CogsErrorHandler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occured in {func.__name__}: {e}. Error code: [205]")
    return wrapper

class Cogs:
    def __init__(self, path=None):
        self.CogPath = path or os.path.join(os.getcwd(), "cogs")
        if not os.path.exists(self.CogPath):
            raise CogsOSError("'cogs' directory does not exist", error_code = 101)
        
        self.cogs_loader = {}
        self.cog_names = self.getCogs()
        self.loadCogs()
        
    @CogsErrorHandler
    def loadCogs(self):
        for cog in self.cog_names:
            cog_path = os.path.join(self.CogPath, f"{cog}.py")
            spec = importlib.util.spec_from_file_location(cog, cog_path)
            if spec is None:
                print(f"Could not load the spec for {cog}")
                continue
            
            try:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                setattr(self, cog, module)

            except Exception as e:
                continue

    @CogsErrorHandler
    def __getitem__(self, cog_name):
        return self.cogs_loader[cog_name]
                
    def getPath(self):
        return self.CogPath
    
    @CogsErrorHandler
    def getCogs(self):
        return self.cog_names
```

### Test Code

```python
from CogForge import Cogs
from cogs import si

coghandler = Cogs()

# Example usage
coghandler.si.TestFunction("Hi")
```

With `si` being the cog/module in the Cogs folder.

## Documentation 📚

For full documentation, including advanced features and guides, visit [CogForge Documentation](#).

## Contributing 🤝

We welcome contributions! See our `CONTRIBUTING.md` file for more details on how to get started.



## License 📄

CogForge is released under the MIT License. See the LICENSE file for more details.

## Support 🆘

If you encounter any problems or have suggestions, please file an issue on the GitHub repository.

---

Happy Coding! 🎈
