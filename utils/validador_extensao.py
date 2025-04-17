from fastapi import HTTPException
import os

# Verificar a extensão do arquivo
def validar_arquivo(filename: str):
    extensoes_validas = ['.mp3', '.wav', '.ogg']

    # recupera a extensão do arquivo
    extensao = os.path.splitext(filename)[1]

    if extensao.lower() not in extensoes_validas:
        raise HTTPException(status_code=400, detail=f"Formato de arquivo inválido: {extensao}")
    return extensao