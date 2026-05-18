import logging
from secom.app.services.user_service import UserService
from secom.app.schemas.user_schema import UserSchema

logger = logging.getLogger("uvicorn.error")


class UserController :

    def __init__(self):
        pass

    def save_user(self, user_schema: UserSchema) :
        logger.info("[Controller] save_user 진입 — %s", user_schema.model_dump())
        user_service = UserService()
        user_service.save_user(user_schema)