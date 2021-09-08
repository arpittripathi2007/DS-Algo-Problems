class Person:
    def __init__(self, id):
        self.id = id
        self.__about = f'{self.id} yes'

sam = Person(100)
print(sam.__about)

sam.__dict__['age'] = 49

print (sam.age + len(sam.__dict__))