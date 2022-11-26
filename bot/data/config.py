import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = str(os.getenv("BOT_TOKEN"))
BOT_TOKEN1: str = str(os.getenv("BOT_TOKEN1"))
OWNER: int = int(os.getenv("OWNER"))

admins_id = [
    5128237746
]
