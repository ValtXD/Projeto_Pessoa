from animal import Gato, Cachorro, Animal


def emitir_som(animal):
    animal.som()

# Testando com diferentes animais
cachorro = Cachorro()
gato = Gato()

emitir_som(cachorro)  # Saída: O cachorro faz: Au Au!
emitir_som(gato)      # Saída: O gato faz: Miau!

# Criando uma classe Pássaro para testar a função
class Passaro(Animal):
    def som(self):
        print("O pássaro faz: Piu Piu!")

passaro = Passaro()
emitir_som(passaro)  # Saída: O pássaro faz: Piu Piu!