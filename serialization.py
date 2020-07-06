""" This is responsible for serializing and saving objects """
import pickle


class Pack:
    """
    Used for packing objects with pickle serialization
    """
    @staticmethod
    def save(cls: object, path: str):
        """ Pickles the given object and saves it in the selected path """
        with open(path, 'wb') as f:
            pickle.dump(cls, f)

    @staticmethod
    def load(path: str):
        """ Loads the pickled file and returns the un-serialized object """
        with open(path, 'rb') as f:
            obj = pickle.load(f)

        return obj
