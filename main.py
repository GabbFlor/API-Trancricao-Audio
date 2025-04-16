import whisper
from fastapi import FastAPI, File, UploadFile, HTTPException
import tempfile
import os

app = FastAPI()
model = whisper.load_model("base")

# Verificar a extensão do arquivo
def checar_extensao_arquivo(filename: str):
    extensoes_validas = ['.mp3', '.wav', '.ogg']

    # recupera a extensão do arquivo
    extensao = os.path.splitext(filename)[1]

    if extensao.lower() not in extensoes_validas:
        raise HTTPException(status_code=400, detail=f"Formato de arquivo inválido: {extensao}")
    return extensao

# Cria a função para receber o áudio (em "file: UploadFile" recebe, e em "File(...)" diz que o arquivo é obrigatório) 
@app.post("/transcrever/")
async def upload_audio(file: UploadFile = File(...)):
    checar_extensao_arquivo(file.filename)

    # Armazena os bytes do áudio
    audio = await file.read();

    # Salva um arquivo temporário do áudio para o whisper poder transcrever:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(audio)
        temp_audio = tmp.name
    
    # Transcrever áudio para texto
    resultado = model.transcribe(temp_audio, language="pt")

    # Retorna o body da requisição
    return {
        "transcricao": resultado["text"]
    }
    