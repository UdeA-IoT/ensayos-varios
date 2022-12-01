# Fase 3

## Descripción

Creación del API para controlar el arduino

### Software

#### Requisitos

Librerias necesarias

### Puesta en marcha del entorno

```bash
python -m venv env
.\env\Scripts\activate        # Windows
pip install -r requirements.txt
pip freeze
```

Verificar que se esta en el entorno.


```py 
#Python
from typing import Optional
from enum import Enum
import serial

#Pydantic
from pydantic import BaseModel
from pydantic import Field

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()
app.serial = None

@app.get("/")
def home():
    return {"App": "Ready"}

@app.get("/connect")
def connect(): 
    print("Iniciando conexión...")
    app.serial = serial.Serial('COM8',115200)
    if app.serial == None:
        return {"Connection": "Fail"}
    else:
        return {"Connection": "Open"}

@app.get("/disconnect")
def disconnect():
    app.serial.close()
    return {"Connection": "Close"}

@app.get("/on")
def led_on():
    app.serial.write('1'.encode())
    return {"led":"on"}

@app.get("/off")
def led_off():
    app.serial.write('0'.encode())
    return {"led":"off"}
```


### Hardware

Archivo fritzing

## Prueba

```bash
uvicorn back_end:app --reload
```

# Referencias

1. [FastAPI](https://fastapi.tiangolo.com/)
2. [StackOverflow[python global variable in fastApi not working as normal]](https://stackoverflow.com/questions/63949240/python-global-variable-in-fastapi-not-working-as-normal)
3. [Using FastAPI to Build Python Web APIs](https://realpython.com/fastapi-python-web-apis/)
