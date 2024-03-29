from src.lib.DataStructure import DataStructure


class HyperParameterStorage(DataStructure):
    def __init__(self):
        self.parameterStorage = dict()

    def set(self, name, value):
        self.parameterStorage[name] = value
        return self

    def set_multi(self, parameters: dict):
        for parameterName in parameters.keys():
            self.set(parameterName, parameters[parameterName])
        return self

    def exists(self, name) -> bool:
        return name in self.parameterStorage.keys()

    def get(self, name):
        assert self.exists(name), 'hyper parameter ' + name + ' not found'
        return self.parameterStorage[name]

    def find(self, name):
        if self.exists(name):
            return self.parameterStorage[name]
        return None

    def get_all(self):
        return self.parameterStorage

    def __repr__(self):
        output = ''
        for key in self.parameterStorage.keys():
            output += (str(key) + ':\n' + str(self.parameterStorage[key]) + '\n\n')
        return output
