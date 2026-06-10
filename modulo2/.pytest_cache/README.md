# Projeto CI/CD com GitHub Actions

## Repositório

Acesse o projeto no GitHub: [cursoCICD](https://github.com/seu-usuario/cursoCICD)

---

## Pipeline CI/CD

O projeto utiliza GitHub Actions para automatizar a execução de testes.

### Status da Execução

Após fazer `push`, acesse a aba **Actions** do repositório no GitHub para visualizar o status da execução dos testes.

---

## Elementos do GitHub Actions

### `on`
Define **quando** o pipeline deve ser acionado. No nosso caso:
- `push` na branch `main`
- `pull_request`

### `jobs`
Define as **tarefas** que serão executadas. No nosso projeto existe um job chamado `test`.

### `runs-on`
Especifica o **ambiente** onde o pipeline rodará. Usamos `ubuntu-latest`.

### `steps`
Lista os **passos** que serão executados em sequência dentro de um job.

### `uses`
Chama **ações prontas** do GitHub ou da comunidade. Exemplos:
- `actions/checkout@v4` - baixa o código
- `actions/setup-python@v5` - instala Python

### `run`
Executa **comandos** diretamente no terminal. Exemplos:
- `pip install -r requirements.txt` - instala dependências
- `pytest` - executa os testes

---

## Como Executar Localmente

1. Instale as dependências:
```bash
python -m pip install -r requirements.txt
```

2. Execute os testes:
```bash
python -m pytest --verbose
```

3. Execute o programa:
```bash
python Teste.py
```

---

## Arquivos do Projeto

- `Teste.py` - script principal
- `test_teste.py` - testes unitários
- `requirements.txt` - dependências
- `.github/workflows/ci.yml` - configuração do pipeline

