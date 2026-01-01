# Sobre o projeto

Este projeto é um gerenciador de programas **.exe** para Windows e Linux, que roda diretamente no terminal (CLI).

O objetivo é permitir que o usuário gerencie e execute programas de Windows a partir de comandos no terminal, de forma simples, leve e sem interface gráfica.

No Linux, os executáveis são rodados utilizando o Wine.

# Como usar

1. Clone este repositório

2. Instale as dependências listadas em requirements.txt

3. Renomeie o arquivo .env.example para .env

4. Crie uma pasta para armazenar os executáveis que deseja gerenciar

5. No arquivo .env, informe o caminho da pasta que contém seus executáveis

6. No terminal, abra a pasta do projeto e execute:

```bash
python main.py listar-programas
```

Para executar um programa:

```bash
python main.py executar nome-do-programa
```


# Objetivo do projeto

Este projeto foi desenvolvido exclusivamente para fins de estudo.

Ele simula, de forma simplificada, funcionalidades presentes em ferramentas como o Heroic, com o objetivo de entender como funciona o processo de gerenciamento e execução de programas multiplataforma via terminal.

Não pretende substituir ferramentas já consolidadas, mas sim servir como aprendizado e experimentação.

# Tecnlogias usadas

- Python
- Typer (CLI)
- InquirerPy (menus interativos)
- Wine (execução de .exe no Linux)
- dotenv (configuração)