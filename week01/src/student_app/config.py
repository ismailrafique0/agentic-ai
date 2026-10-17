import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Default SIS")
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
MAX_STUDENTS = int(os.getenv("MAX_STUDENTS", "50"))