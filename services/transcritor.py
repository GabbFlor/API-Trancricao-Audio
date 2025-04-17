import whisper

model = whisper.load_model("base")

def trasncrever_audio(file_path: str) -> str:
    result = model.transcribe(file_path, language="pt")

    return result["text"]