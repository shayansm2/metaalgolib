class HyperParameterStorage(object):
    def __init__(self):
        self.parameterStorage = dict()

    def set_hyper_parameter(self, name, value):
        self.parameterStorage[name] = value
        return self

    def set_hyper_parameters(self, parameters: dict):
        for parameterName in parameters.keys():
            self.set_hyper_parameter(parameterName, parameters[parameterName])
        return self

    def get_hyper_parameter(self, name):
        assert name in self.parameterStorage.keys(), 'hyper parameter not found'

        return self.parameterStorage[name]

    def get_all(self):
        return self.parameterStorage

    def __repr__(self):
        output = ''
        for key in self.parameterStorage.keys():
            output += (str(key) + ':\n' + str(self.parameterStorage[key]) + '\n\n')
        return output
