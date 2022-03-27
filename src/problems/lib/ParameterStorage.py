from src.lib.DataStructure import DataStructure


class ParameterStorage(DataStructure):
    def __repr__(self):
        parameters = vars(self)

        output = ''
        for name in parameters.keys():
            output += (str(name) + ': ' + str(parameters[name]) + '\n')
        return output
