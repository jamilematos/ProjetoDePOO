from veiculo import Veiculo

class Barco(Veiculo):
    def __init__(self, marca, modelo, ano, capacidade):
        super().__init__(marca, modelo, ano)
        self.capacidade = capacidade

    def acelerar(self):
        print(f"O barco {self.modelo} está navegando a toda velocidade!")

    def frear(self):
        print(f"O barco {self.modelo} está desacelerando!")

    def exibir_informacoes(self):
        informacoes_gerais = super().exibir_informacoes()
        return f"{informacoes_gerais}, Capacidade: {self.capacidade} pessoas"
