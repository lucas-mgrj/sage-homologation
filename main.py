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
