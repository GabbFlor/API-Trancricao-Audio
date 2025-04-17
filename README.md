# API para transcrição de áudio

## Rodando o projeto:
Para instalar a biblioteca de transcrição de áudio:
```bash
    pip install git+https://github.com/openai/whisper.git
```

Para instalar a biblioteca que lida com as requisições HTTP (aceitando arquivos):
```bash
    pip install fastapi uvicorn python-multipart
```

Uvicorn serve para executar o servidor com FastAPI e executar as alterações rapidamente para teste (em produção seria necessário usar outra ferramenta para executar o servidor):
```bash
    pip install uvicorn
```


Para rodar a API (somente após instalar as dependencias com pip):
```bash
    uvicorn main:app --reload
```


## Rotas do projeto:
Principal rota:
```bash
    http://127.0.0.1:8000/transcrever/
```

Para requisição funcionar, precisa colocar o body como: "Form Data", e enviar o arquivo de áudio da seguinte maneira: 
<p align="center">
  <img src="./imgs_md/exemplo_req.png" alt="Exemplo Requisição"/>
</p>

Além disso, para a requisição funcionar corretamente, deverá ser inserido no header o campo x-api-key:
```json
    x-api-key: "SUA_API_KEY"
```

Esse campo pode ser alterado em:
```bash
    ./services/security.py
```