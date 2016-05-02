from twisted.internet import reactor
import os,imp
from interface import Interface

class FoxbotInterface(Interface):
    CMDS="cmds/"
    def load_modules(self, path):
        mods = {}
        if path:
            dir_list = os.listdir(path)
            for fname in dir_list:
                name, ext = os.path.splitext(fname)
                if ext == '.py' and not name == '__init__':
                    f, filename, descr = imp.find_module(name, [path])
                    mods[name] = imp.load_module(name, f, filename, descr)
        return mods
    
    def start(self, *args, **kwargs):
        self.load_modules(FoxbotInterface.CMDS)
        try:
            for k in self.registry: 
                if k != "foxbotsinterface":
                    print(k)
                    self.registry[k].start(*args,**kwargs)
        except Exception as e:
            print("Interface Start Error: %s"%(str(e)))