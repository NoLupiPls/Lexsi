import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = str(os.getenv("BOT_TOKEN"))
BOT_TOKEN1: str = str(os.getenv("BOT_TOKEN1"))
OWNER: int = int(os.getenv("OWNER"))
LANG: str = str(os.getenv("LANG"))
I18N_DOMAIN: str = str(os.getenv("I18N_DOMAIN"))

app_dir: Path = Path(__file__).parent.parent
LOCALES_DIR = app_dir / "locales"

admins_id = [
    5128237746
]
