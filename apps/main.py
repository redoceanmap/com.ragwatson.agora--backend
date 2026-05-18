from secom.app.controllers import user_controller
from secom.app.schemas import user_schema
import logging
import os
from pathlib import Path
from dotenv import load_dotenv
import httpx

from fastapi import Depends, FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
import json
from pydantic import BaseModel
from database import get_db
from matrix.app.keymaker import get_keymaker, GEMINI_MODEL
from secom.app.schemas.user_schema import UserSchema
from secom.app.controllers.user_controller import UserController

logger = logging.getLogger("uvicorn.error")

load_dotenv(Path(__file__).parents[1] / ".env")

app = FastAPI(title="Main page")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "http://127.0.0.1:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

keymaker = get_keymaker()

from titanic.app.james_controller import JamesController
from doro.app.doro_director import DoroDiretor


@app.get("/")
def read_root():
    content = {"message": "FAST API 메인 페이지", "docs": "/docs"}
    json_str = json.dumps(content, ensure_ascii=False, indent=4)
    return Response(content=json_str.encode("utf-8"), media_type="application/json; charset=utf-8")

class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat(req: ChatRequest):
    if keymaker.client is None:
        return {"error": "Gemini API key가 설정되지 않았습니다."}
    try:
        response = keymaker.client.models.generate_content(model=GEMINI_MODEL, contents=req.message)
        return {"reply": response.text}
    except Exception as e:
        return {"error": str(e)}


# 회원가입
class SignupRequest(BaseModel):
    userId: str
    password: str
    nickname: str
    email: str


@app.post("/signup")
async def signup(req: SignupRequest):
    logger.info(
        "회원가입 요청 수신 — 아이디: %s / 닉네임: %s / 이메일: %s",
        req.userId, req.nickname, req.email,
    )

    user_schema = UserSchema(
        userId=req.userId,
        password=req.password,
        nickname=req.nickname,
        email=req.email,
        role="user",
    )

    user_controller = UserController()
    user_controller.save_user(user_schema)

    return {"message": "회원가입 요청을 받았습니다.", "userId": req.userId, "nickname": req.nickname, "email": req.email}


@app.get("/weather")
async def get_weather(lat: float, lon: float):
    api_key = os.getenv("OPENWEATHER_API_KEY", "")
    if not api_key:
        return {"error": "OpenWeather API key가 설정되지 않았습니다."}
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params={"lat": lat, "lon": lon, "appid": api_key, "units": "metric", "lang": "kr"},
            )
            data = res.json()
        return {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"],
            "humidity": data["main"]["humidity"],
        }
    except Exception as e:
        return {"error": str(e)}


@app.get("/titanic/data")
def read_titanic_data():
    james = JamesController()
    return james.get_data()


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

@app.get("/db-check")
async def check_db(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT NOW();"))
        now = result.scalar()
        return {"status": "success", "neon_time": str(now)}
    except Exception as e:
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

    