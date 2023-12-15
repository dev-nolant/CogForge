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
        self.cog_names
