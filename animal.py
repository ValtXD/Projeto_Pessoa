class Animal:
    def som(self):
        pass

    def mover(self):
        print("O animal está se movendo.")

class Cachorro(Animal):
    def som(self):
        print("O cachorro faz: Au Au!")

class Gato(Animal):
    def som(self):
        print("O gato faz: Miau!")