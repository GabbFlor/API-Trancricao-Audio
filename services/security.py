from typing import Optional
from fastapi import Header, HTTPException

API_KEY = "SUA_API_KEY"

def verificar_api_key(x_api_key: Optional[str] = Header(None, alias="x-api-key")):
    if x_api_key != API_KEY or not x_api_key:
        raise HTTPException(status_code=403, detail="Api Key inválida ou não inserida.")