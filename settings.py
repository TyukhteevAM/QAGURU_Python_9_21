import os
from dotenv import load_dotenv
import pydantic


class Config(pydantic.BaseModel):
    load_dotenv()
    user_name: str = os.getenv('USER_NAME')
    access_key: str = os.getenv('ACCESS_KEY')


config = Config()
