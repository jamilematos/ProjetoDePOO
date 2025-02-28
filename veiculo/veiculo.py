from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

    def exibir_informacoes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"
