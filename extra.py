class Namespace(metaclass=type):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    def append(self, key:str, value):
        self.__dict__[key] = value
    def debug(self):
        return self.__dict__
    
class ConstGroup(metaclass=type):
    def __init__(self):
        self._constants = {}
        
    def __setattr__(self, name: str, value):
        if name in self._constants:
            raise ConstError(f"Const '{name}' Cann't Be Modified!")
        self._constants[name] = value
        
    def __getattr__(self, name: str):
        if name not in self._constants:
            raise ConstError(f"Const '{name}' Not Found!")
        return self._constants[name]
    
    def list_constants(self):
        return self._constants.items()

class ConstError(TypeError):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
    
class Copyright:
    def __init__(self, name:str, version:str, authors:list, updatetime:str, team:str):
        self.infogroup = ConstGroup()
        self.infogroup.name = name
        self.infogroup.version = version
        self.infogroup.author = authors
        self.infogroup.updatetime = updatetime
        self.infogroup.team = team
        
    def generate_readme(self, path:str, otherinfo:str=""):
        text = f"""\
# {self.infogroup.name} {self.infogroup.version}({self.infogroup.updatetime})
Authors: {', '.join(self.infogroup.author)}

{otherinfo}

Copyright © {self.infogroup.team} All Rights Reserved.
"""
        with open(path, "w", encoding="utf-8") as f:
            f.truncate(0)
            f.write(text)
    
if __name__ == "__main__":
    print("This is a module of FedpyLib.You should read 'example/extra.py' to understand the usage.")