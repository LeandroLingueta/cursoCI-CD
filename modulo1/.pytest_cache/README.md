
# 1 Como executar o projeto localmente:
 para executar o "Teste.py" onde esta minhas duas funções, basta escrever "python Teste.py" no terminal para executar



# 2 Como rodar os testes:
Estou usando o windows, entao o comando certo para rodar o codigo é "python -m pytest", o "pytest --verbose" não esta funcionado por isso, porem se estiver usando linux ou wsl irá funcionar

# 3 Como funciona o pipeline criado:
Dispara sempre que você:

faz push para a branch main
abre ou atualiza um pull_request
O GitHub Actions cria um ambiente com:

ubuntu-latest
Executa estes passos:

actions/checkout@v4

baixa o código do repositório para o runner
actions/setup-python@v5 com python-version: "3.12"

instala o Python 3.12 no ambiente
python -m pip install --upgrade pip && pip install -r requirements.txt

atualiza o pip
instala as dependências do projeto listadas em requirements.txt
pytest

executa os testes automatizados