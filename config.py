from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")

BOT_TOKEN = getenv("BOT_TOKEN", " ")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", " "))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/9656bed2d9359c9675f52.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/9656bed2d9359c9675f52.jpg")

SESSION = getenv("SESSION", "AgGfBwsAbzYp3-ngXz2hEdJAZ5Afz90dHa3_vEDk07GhBpkDDQF0jCiZmHRr8D_iPWCqTBG7jj6YkprP6dSuGAXH1WgQSP8C8ZpGa5x8z4I3WsMzXStoRap-YLgd1Qa0mXkRIFNOKEz_1_-ZILRwubgzTc4mKOji2uPGFTgUD3mju3GL2WVAgBecC_uI1i-yjo_ziJ8Z7JVfJAYK0mBWDpJKWjZ1qFSgOkwGwbOWfnAvbl2WW3IQW_QJGbs1MQc8iofOvQ9WQZUwLR211hrRLnDOhNNeK9qsJfwqL_jjRDpmU4UMSs5z7Gho9DFy9dY36gYjeEwHMD0WWJCr6GrAyQQ_fnRpSQAAAAFYbzfsAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kasbinxeyallari1")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ATO_RESMl")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5637445914").split()))


FAILED = "https://telegra.ph/file/9656bed2d9359c9675f52.jpg"
