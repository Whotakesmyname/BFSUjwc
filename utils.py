# coding:utf-8
# Workaround for Python Redis who crys for string input.
# Harrisson Chen @ 2017
import pickle


class Serialize:

    @staticmethod
    def serialize(query):
        b = pickle.dumps(query)
        s = b.decode('latin')
        return s

    @staticmethod
    def unserialize(s: str):
        b = s.encode('latin')
        q = pickle.loads(b)
        return q
