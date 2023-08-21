# ---------------------------------Automalógica---------------------------------
# Nome do Arquivo: AutoFetchAPI.py
# Descrição: API de Interface entre SAGE e SISCON
#
# Autor: Lucas Nascimento
# Data: 08/08/2023
#
# Versão: 1.0
#
# Histórico de Modificações:
#     1.0 - 27/03/2023 - Esboço de código.
# Notas:
#     — Existem dois modos de envio, teste e produção.
# ------------------------------------------------------------------------------
import os
from random import randint
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

# Comando para iniciar o servidor: uvicorn main:app --host localhost --port 8080 --reload

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get('/')
async def af_root():
    return {'Status': 'Interface Ativa'}


@app.get('/CreateHash')
async def af_return_hash(user: str = Query(), pwd: str = Query):
    import hashlib
    sha256_hash = hashlib.sha256(f'{user}{pwd}'.encode()).hexdigest()
    return {'hash': sha256_hash}


@app.get('/GetNameOfFiles')
async def af_get_name_of_files():
    files = os.listdir()
    return {'files': [files]}


@app.get('/GetOneFile')
async def af_get_one_file():
    files = os.listdir()
    file = files[randint(0, len(files)-1)]
    return {'file': file}


@app.get('/FetchFile')
async def af_fetch_file(file_name: str = Query(default=None), extension: str = Query(default='pdf')):
    if file_name is None:
        return {'Error': 'Nome do arquivo não informado'}
    else:
        return FileResponse(path=f"{file_name}.{extension}", filename=f"{file_name}.{extension}")
