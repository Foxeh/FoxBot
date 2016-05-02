import types

class InterfaceMeta(type):
    def __init__(cls, name, bases, dct):
        super(InterfaceMeta, cls).__init__(name, bases, dct) 
        if not hasattr(cls, 'registry'):
            cls.registry = {}
            cls.funcMap = {}
        else:
            interface_id = name.lower()
            cls.registry[interface_id] = cls()  
            for attrname in dir(cls.registry[interface_id]):
                if attrname.startswith('__'): continue
                if attrname not in cls.funcMap:
                    attr = getattr(cls.registry[interface_id], attrname)
                    if type(attr) == types.MethodType:
                        cls.funcMap[attrname] = interface_id   
                                
class Interface(object):
    __metaclass__ = InterfaceMeta

    def start(self, *args, **kwargs):
        pass 
    
    def stop(self, *args, **kwargs):
        pass
            
    def getFunc(self,funcName):
        interfaceId = self.funcMap[funcName]
        return getattr(self.registry[interfaceId], funcName)