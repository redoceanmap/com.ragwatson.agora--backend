import logging
from secom.app.schemas.user_schema import UserSchema
from secom.app.models.user_model import UserModel

logger = logging.getLogger("uvicorn.error")


class UserRepository :

    def __init__(self):
        pass

    def save_user(self, user_schema: UserSchema) :
        logger.info("[Repository] save_user 진입 — %s", user_schema.model_dump())