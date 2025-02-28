Este projeto tem como objetivo criar um sistema que simula o comportamento de diferentes tipos de veículos, como moto, barco e carro, utilizando conceitos da programação orientada a objetos. Cada tipo de veículo possui atributos e comportamentos específicos, como a marca, o modelo, o ano, a cilindrada (para a moto), a capacidade (para o barco), e o número de portas (para o carro). Além disso, cada veículo tem métodos próprios para acelerar e frear, permitindo que o código mostre as ações desses veículos.
A estrutura do código define uma classe Veiculo como base, com informações comuns, e depois cria classes filhas para Moto, Barco e Carro. Cada classe filha herda os atributos e métodos da classe Veiculo, mas também pode sobrescrever ou adicionar métodos específicos para o comportamento de aceleração e frenagem. No código principal, o programa instancia objetos dessas classes e chama os métodos para acelerar e frear, exibindo o comportamento de cada veículo.
Quando o código é executado, o terminal exibe informações detalhadas sobre cada veículo, incluindo marca, modelo, ano, e características específicas (como cilindrada para a moto ou capacidade para o barco). Além disso, o comportamento de aceleração e frenagem é exibido, como por exemplo: "A moto CB500 está acelerando!" ou "O barco 242X está desacelerando!". Essa saída demonstra como os diferentes veículos se comportam de forma única, mesmo compartilhando atributos comuns. Isso reflete o uso de conceitos de herança e polimorfismo da programação orientada a objetos.
Como usar:
1. Clone o repositório
Primeiro, você precisa clonar o repositório para sua máquina local. Abra o terminal ou o prompt de comando e execute o seguinte comando:
git clone https://github.com/jamilematos/ProjetoDePOO

2. Depois de clonar o repositório, entre no diretório do projeto com o comando:
cd veiculo

3. Instale as dependências (se houver)
Se o seu projeto depender de pacotes externos (por exemplo, requirements.txt), você deve instalar as dependências. Caso contrário, você pode pular essa etapa.
Se houver um arquivo requirements.txt, execute:
pip install -r requirements.txt

4. Execute o código
Agora, para ver a simulação de aceleração e frenagem dos veículos, execute o script principal:
python main.py
Isso irá rodar o código e mostrar no terminal o comportamento de aceleração e frenagem dos veículos, como por exemplo:

Marca: Honda, Modelo: CB500, Ano: 2022, Cilindrada: 500cc
A moto CB500 está acelerando!
A moto CB500 está freando!

Marca: Yamaha, Modelo: 242X, Ano: 2021, Capacidade: 10 pessoas
O barco 242X está navegando a toda velocidade!
O barco 242X está desacelerando!

Marca: Fiat, Modelo: Uno, Ano: 2020, Portas: 4
O carro Uno está acelerando!
O carro Uno está freando!


5. Personalize ou modifique (opcional)
Se você quiser adicionar novos veículos ou modificar as características dos existentes, basta alterar as classes no código. As classes Moto, Carro e Barco estão implementadas em arquivos .py e podem ser personalizadas conforme necessário.
