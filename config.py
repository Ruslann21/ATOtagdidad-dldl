from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "27199243"))
API_HASH = getenv("API_HASH", "0e30888407241b7436e460f0361b021c")

BOT_TOKEN = getenv("BOT_TOKEN", "5586550312:AAGG0Pk3jj2TNTyO_sWY8hC5F57yShUM3Ng")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5637445914"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/364ae0f56299f1dc79966.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/364ae0f56299f1dc79966.jpg")

SESSION = getenv("SESSION", "AgCg3A7P4mDGuHnqt66SyBxi8PQXyMwd4FsUPUjwy7OY6cY8UIPX8Aa2XPR9oSwAvg-p-iuMg-uGX57xWay6OV5BfTZr3Pfv2Z0pg-m5bARipePLyuSuYLUYHvIGyNwPuuopv4s6hMSL68WyiH-UQnr-0MQ-81fWQJnezd2-riWb-I_wM4F0qtvwBtJCrwR0wbfddCQKF4-Id4HggVYyBTGBnLUoye-yFurUIPlrLe3JDu78KN_HPJuHgOoq86TKBZwazVegtbuQVvJPSaclB5yUTP_AtNQGiINERhurOls260tFS93qtDUg6hG4gCSNDLKdVmId1s0mDqN8v9-tm0uRAAAAAVhvN-wA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kasbinx")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ATO_RESMl")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5539983698").split()))


FAILED = "https://telegra.ph/file/364ae0f56299f1dc79966.jpg"
