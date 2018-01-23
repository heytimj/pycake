import json


class CakeModel(object):
    """ Base class from which all models will inherit. """

    def __init__(self, **kwargs):
        self.param_defaults = {}

    def __str__(self):
        return self.as_json_string()

    def __eq__(self, other):
        return other and self.AsDict() == other.as_dict()

    def __ne__(self, other):
        return not self.__eq__(other)

    def as_json_string(self):
        return json.dumps(self.as_dict(), sort_keys=True)

    def as_dict(self):
        data = {}
        for key, value in self.param_defaults.items():
            if isinstance(getattr(self, key, None), (list, tuple, set)):
                data[key] = list()
                for subobj in getattr(self, key, None):
                    if getattr(subobj, 'as_dict', None):
                        data[key].append(subobj.as_dict())
                    else:
                        data[key].append(subobj)
            elif getattr(getattr(self, key, None), 'as_dict', None):
                data[key] = getattr(self, key).as_dict()
            elif getattr(self, key, None):
                data[key] = getattr(self, key, None)
        return data


    