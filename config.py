import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    URI=os.getenv("DATABASE_URI")
    