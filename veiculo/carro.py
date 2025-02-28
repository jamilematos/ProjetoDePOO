from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def acelerar(self):
        print(f"O carro {self.modelo} está acelerando!")

    def frear(self):
        print(f"O carro {self.modelo} está freando!")

    def exibir_informacoes(self):
        informacoes_gerais = super().exibir_informacoes()
        return f"{informacoes_gerais}, Portas: {self.portas}"
