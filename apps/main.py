from fastapi import FastAPI, Response
import json

app = FastAPI(title="Redoceanmap Main Page")

try:
    from titanic.app.james_controller import JamesController
    from doro.app.doro_director import DoroDiretor
except ModuleNotFoundError:
    from apps.titanic.app.james_controller import JamesController
    from apps.doro.app.doro_director import DoroDiretor


@app.get("/")
def read_root():
    content = {"message": "FAST API 메인 페이지", "docs": "/docs"}
    json_str = json.dumps(content, ensure_ascii=False, indent=4)
    return Response(content=json_str.encode("utf-8"), media_type="application/json; charset=utf-8")

@app.get("/titanic/data")
def read_titanic_data():
    james = JamesController()
    df = james.get_data()
    
    return df.to_dict(orient="records")


@app.get("/titanic/count")
def read_titanic_count():
    james = JamesController()
    count = james.get_count()

    return {"count": count}

@app.get("/titanic/tree")
def read_titanic_tree():
    james = JamesController()
    tree = james.get_tree()

    return {"tree": tree}

@app.get("/titanic/model")
def read_titanic_model() :
    james = JamesController()
    model = james.get_model_name()
    accuracy = james.get_accuracy()

    return {"model" :model, "accuracy" : accuracy}

@app.get("/titanic/count/survived")
def read_titanic_count_survived():
    james = JamesController()
    count = james.get_survived()

    return {"survived": count}

@app.get("/titanic/count/dead")
def read_titanic_count_dead():
    james = JamesController()
    count = james.get_dead()

    return {"dead": count}


@app.get("/doro/data")
def read_doro_data():
    doro_director = DoroDiretor()
    df = doro_director.get_data() 
    
    return df.to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

    