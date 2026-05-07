from fastapi import FastAPI, Response
import json 

app = FastAPI(title="Redoceanmap Main Page")

try:
    from titanic.app.james import James
    from doro.app.doro_director import Doro_diretor
except ModuleNotFoundError:
    from apps.titanic.app.james import James
    from apps.doro.app.doro_director import Doro_diretor


@app.get("/")
def read_root():
    content = {"message": "FAST API 메인 페이지", "docs": "/docs"}
    json_str = json.dumps(content, ensure_ascii=False, indent=4)
    return Response(content=json_str.encode("utf-8"), media_type="application/json; charset=utf-8")

@app.get("/titanic/data")
def read_titanic_data():
    james = James()
    df = james.get_data()
    
    return df.to_dict(orient="records")

@app.get("/doro/data")
def read_doro_data():
    doro_director = Doro_diretor()
    df = doro_director.get_data() 
    
    return df.to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn
    # uvicorn 실행 명령어 설정
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

    