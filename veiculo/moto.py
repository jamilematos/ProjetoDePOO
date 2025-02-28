from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada

    def acelerar(self):
        print(f"A moto {self.modelo} está acelerando!")

    def frear(self):
        print(f"A moto {self.modelo} está freando!")

    def exibir_informacoes(self):
        informacoes_gerais = super().exibir_informacoes()
        return f"{informacoes_gerais}, Cilindrada: {self.cilindrada}cc"
