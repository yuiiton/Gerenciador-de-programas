import os
import subprocess
import platform
import shutil

def buscar_programas(diretorio: str):
    if not os.path.exists(diretorio):
        raise FileNotFoundError("Diretório não encontrado ou não existe.")
    
    lista_programas = []

    for item in os.listdir(diretorio):
            if item.endswith(".exe"):
                caminho_completo = os.path.join(diretorio, item)

                esquema = {
                    "nome": item,
                    "diretorio": caminho_completo
                }
                lista_programas.append(esquema)
    return lista_programas


def executar_programa(diretorio_programa: str):
    sistema_operacional = platform.system().lower()

    if not os.path.exists(diretorio_programa):
        raise FileNotFoundError("Diretório do programa não encontrado ou não existe.")

    try:
        if sistema_operacional == "windows":
            subprocess.Popen([diretorio_programa])

        elif sistema_operacional == "linux":
            if not shutil.which("wine"):
                print("Wine não está instalado")
                return

            subprocess.Popen(["wine", diretorio_programa])

        else:
            return {"sucesso": False, "erro": "Sistema operacional não suportado"}

        return {"sucesso": True}

    except Exception as e:
        return {"sucesso": False, "erro": str(e)}