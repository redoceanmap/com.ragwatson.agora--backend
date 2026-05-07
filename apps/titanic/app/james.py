from fastapi import FastAPI
from apps.titanic.app.walter import Walter

app = FastAPI(title="Titanic (James)")

class James:
    def __init__(self):
        pass

    def get_data(self):
        w = Walter()
        return w.get_data()