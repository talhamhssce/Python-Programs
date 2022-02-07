#object:

class Person:
    #fields
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('I am a constructor')
    def display(self):
        print('I am a method', self.name, self.age)

#object is ceated here of class person and iy is assigned to talha
talha = Person('Talha', 22)
talha.display()        