import re


class Pythonize:
    @staticmethod
    def class_name(s):
        s = s.replace('_', '-').replace('.', '-').replace(' ', '-')
        s = ''.join([c.capitalize() for c in s.split('-')])
        s = re.sub('[^0-9a-zA-Z_]', '', s)
        return re.sub('^[^a-zA-Z_]+', '', s)

    @staticmethod
    def method_name(s):
        s = s.replace('_', '-').replace('.', '-').replace(' ', '-')
        s = ''.join([c.lower() for c in s.split('-')])
        s = re.sub('[^0-9a-zA-Z_]', '', s)
        return re.sub('^[^a-zA-Z_]+', '', s)
