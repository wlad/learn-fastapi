#!/usr/bin/env python3

from fastapi import FastAPI, Query
from enum import Enum
from typing import Optional
from pydantic import BaseModel



app = FastAPI()

@app.get('/read_file/{file_path:path}')
def read_file(file_path: str):
    """Liest eine Datei und gibt sie als 'content' im Browser aus.

    Args:
        file_path (str): Pfad zur Datei

    Returns:
        json: Ein JSON Objekt
    """
    a = open(file_path).read()
    return {'content': f'{a}'}
