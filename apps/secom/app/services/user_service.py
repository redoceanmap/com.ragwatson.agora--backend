import logging
from secom.app.repositories.user_repository import UserRepository
from secom.app.schemas.user_schema import UserSchema

logger = logging.getLogger("uvicorn.error")


class UserService :

    def __init__(self):
        pass

    def save_user(self, user_schema: UserSchema) :
        logger.info("[Service] save_user 진입 — %s", user_schema.model_dump())
        user_repository = UserRepository()
        user_repository.save_user(user_schema)