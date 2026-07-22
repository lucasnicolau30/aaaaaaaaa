# Ambientes Virtuais (venv)

**venv:** ambiente isolado que cria uma cópia independente do Python para um projeto específico, com suas próprias dependências e versões de pacotes, sem interferir no Python global do sistema nem em outros projetos.

## Vantagens

- Gerenciar dependências
- Versões
- Pacotes
- Sem conflitos entre projetos diferentes

## Criar e ativar um ambiente (Windows)

```powershell
python -m venv venv
.\venv\Scripts\activate
```

Para sair do ambiente ativo, use `deactivate`. Depois disso, é só ativar de novo com `.\venv\Scripts\activate` quando precisar.

```powershell
deactivate
.\venv\Scripts\activate
```

## Criar e ativar um ambiente (macOS/Linux)

```bash
python3 -m venv my_env
source my_env/bin/activate
```

## Instalar pacotes e salvar dependências

Depois de ativar o ambiente, os pacotes instalados ficam isolados dentro dele:

```bash
pip list
pip install -r requirements.txt
```

Para gerar o arquivo de dependências do projeto (usado pelo `pip install -r`):

```bash
pip freeze > requirements.txt
```

## Resumo

- Criar um ambiente
- Ativar um ambiente
- Instalar pacotes individualmente
- Instalar pacotes a partir de um arquivo
- Salvar os pacotes