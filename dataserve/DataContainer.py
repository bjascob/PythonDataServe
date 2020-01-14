import gzip
import pickle


class DataContainer(object):
    def __init__(self, load_fn=None):
        if load_fn is not None:
            self.load(load_fn)

    def add_object_data(self, obj, add_private=False):
        for key, value in vars(obj).items():
            if not key.startswith('_') or add_private:
                setattr(self, key, value)

    def save(self, filename):
        with self._open(filename, 'wb') as f:
            pickle.dump(self.__dict__, f, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self, filename):
        with self._open(filename, 'rb') as f:
            self.__dict__ = pickle.load(f)

    @staticmethod
    def _open(filename, mode):
        if filename.split('.')[-1] == 'gz':
            return gzip.open(filename, mode)
        return open(filename, mode)
