import whisper

# se a transcrição ficar imprecisa, da pra usar:
# tiny, base, small, medium ou large. 
# Quanto maior for o model, mais lento e mais necessidade de recursos
model = whisper.load_model("base")

def transcrever_audio(file_path: str) -> str:
    result = model.transcribe(file_path, language="pt")

    return result["text"]