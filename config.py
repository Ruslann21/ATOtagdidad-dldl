from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "27199243"))
API_HASH = getenv("API_HASH", "0e30888407241b7436e460f0361b021c")

BOT_TOKEN = getenv("BOT_TOKEN", "5586550312:AAGbeld23hdwnsEBu7QgBP6bY2ZaHFjJCRw")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5637445914"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/9656bed2d9359c9675f52.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/9656bed2d9359c9675f52.jpg")

SESSION = getenv("SESSION", "AgC5tZzy3C1z2OTcU2OXSTNuBmMFrAvgn9KGP8e7_IXvli9Kv8LxZiFnPV-4JMVUGmt0nZ44_XLPTJgPfg3bBxKKFxYuhrkZWzMHgiN_OU3jgkvofWObV07KIXjwrUu_0wWq_CodJzQUnVnc5Z0tKtmguo5_HcWYNmC_fLA4vQk4qX-Gr4Tos8k3tKI2gUGAcpJt3ywdHhPH0k1JoTRRrKaq1NpCbzIWGQ5G_-EtkLL6X_vzkr_NypbHTdBqcgfjkJO7KicmIZ1-epkE7D51X05VwRMJWa5MI0t7YpSFE5uIwa60QyxSvXhtKxHfwJONmYvMBoKsuPPraXRQ42rQDAJUAAAAAVhvN-wA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kasbinxeyallari1")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ATO_RESMl")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5637445914").split()))


FAILED = "https://telegra.ph/file/9656bed2d9359c9675f52.jpg"
