# API para transcrição de áudio

Para instalar a biblioteca de transcrição de áudio:
```bash
    pip install git+https://github.com/openai/whisper.git
```

Para instalar a biblioteca que lida com as requisições HTTP (aceitando arquivos):
```bash
    pip install fastapi uvicorn python-multipart
```

Uvicorn serve para executar o servidor com FastAPI e executar as alterações rapidamente para teste:
```bash
    pip install uvicorn
```


Para rodar a API (somente após instalar as dependencias com pip):
```bash
    uvicorn main:app --reload
```

### OBS: todos os pacotes instalados pelo pip, ficam no .venv da pasta raiz do projeto (isso só se estiver usando arch linux, se não provavelmente fica no global)