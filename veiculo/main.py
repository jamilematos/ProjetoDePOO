from carro import Carro
from moto import Moto
from barco import Barco

def testar_veiculos():
    # Criando instâncias de veículos
    carro = Carro("Fiat", "Uno", 2020, 4)
    moto = Moto("Honda", "CB500", 2022, 500)
    barco = Barco("Yamaha", "242X", 2021, 10)

    # Adicionando os veículos em uma lista para testar o polimorfismo
    veiculos = [carro, moto, barco]

    # Testando os métodos
    for veiculo in veiculos:
        print(veiculo.exibir_informacoes())
        veiculo.acelerar()
        veiculo.frear()
        print("-" * 30)

if __name__ == "__main__":
    testar_veiculos()
