class Pessoa:
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")


class Empregado:
    def _init_(self, salario, cargo):
        self.salario = salario
        self.cargo = cargo

    def mostrar_detalhes_emprego(self):
        print(f"Salário: {self.salario}, Cargo: {self.cargo}")


class Gerente(Pessoa, Empregado):
    def _init_(self, nome, idade, salario, cargo, departamento):
        Pessoa._init_(self, nome, idade)
        Empregado._init_(self, salario, cargo)
        self.departamento = departamento

    def mostrar_informacoes_completas(self):
        self.mostrar_informacoes()
        self.mostrar_detalhes_emprego()
        print(f"Departamento: {self.departamento}")