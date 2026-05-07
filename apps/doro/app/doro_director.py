from fastapi import FastAPI
from apps.doro.app.doro_reader import Doro_reader

app = FastAPI(title="Doro (Director)")

class Doro_diretor:
    def __init__(self):
        pass

    def get_data(self):
        d = Doro_reader()
        return d.get_data()