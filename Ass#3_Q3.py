class my_dictionary(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

dict_obj = my_dictionary()

dict_obj.add(1, 'Moiz')
dict_obj.add(2, 'Uddin')

print(dict_obj)