from fastapi import FastAPI, File, UploadFile, Depends
import tempfile
import os

# importando os arquivos que criei para funcionar a API
from services.transcritor import transcrever_audio
from services.security import verificar_api_key
from utils.validador_extensao import validar_arquivo

app = FastAPI()

print("teste")

@app.post("/transcrever/")
async def upload_audio(file: UploadFile = File(...), _=Depends(verificar_api_key)):
    validar_arquivo(file.filename)

    # Armazena os bytes do áudio
    audio = await file.read()

    # Salva um arquivo temporário do áudio para o whisper poder transcrever:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(audio)
        temp_audio = tmp.name
    
    text = transcrever_audio(temp_audio)
    os.remove(temp_audio)

    # Retorna o body da requisição
    return {
        "transcricao": text
    }
    