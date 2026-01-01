import typer
from InquirerPy import inquirer
from backend.pyenv import diretorio_programas
from backend.core import buscar_programas, executar_programa

app = typer.Typer()

@app.command()
def listar_programas():
    try:
        programas = buscar_programas(diretorio_programas)

        if not programas:
            print("Nenhumm programa encontrado.")
            return
        
        contador = 0
        for programa in programas:
            contador += 1
            print(f"{contador}. {programa["nome"]}")
    
    except FileNotFoundError:
        print("Diretório não encontrado.")
        return

    except Exception as e:
        print(f"Erro inesperado: {e}")
        return        


@app.command()
def executar():
    try:
        programas = buscar_programas(diretorio_programas)

        if not programas:
            print("Nenhum programa encontrado.")
            return

        escolhido = inquirer.select(
            message="Escolha um programa para executar (ou aperte CTRL+C para cancelar):",
            choices=[
                {
                    "name": programa["nome"],
                    "value": programa
                 
                }
                for programa in programas
            ]
        ).execute()

        executar_programa(
            escolhido["diretorio"]
        )
        print(f"Iniciando {escolhido['nome']}… ")

    except FileNotFoundError:
        print("Diretório não encontrado.")
        return

    except Exception as e:
        print(f"Erro inesperado: {e}")
        return
    
    except KeyboardInterrupt:
        print("Seleção cancelada.")
        return


if __name__ == "__main__":
    app()
