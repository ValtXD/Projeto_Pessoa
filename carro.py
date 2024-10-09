class Carro:
    def _init_(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_ano(self):
        return self._ano

    def set_ano(self, ano):
        self._ano = ano

    def mostrar_informacoes(self):
        print(f"Marca: {self._marca}, Modelo: {self._modelo}, Ano: {self._ano}")
