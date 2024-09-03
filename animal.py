class Animal:
    def som(self):
        pass
class Cachorro(Animal):
    def som(self):
        print("O cachorro late.")

class Gato(Animal):
    def som(self):
        print("O gato mia.")

animais = [Cachorro(), Gato()]
for animal in animais:
    animal.som()