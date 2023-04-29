from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "22007754"))
API_HASH = getenv("API_HASH", "7f0d6b4d928155eda014acdb5a014620")

BOT_TOKEN = getenv("BOT_TOKEN", "6195626321:AAEdQkOcqe6OIQxwRVFiigXn3f-HvQcmjM8")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5539983698"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/3ac497b59a221257ef441.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/3ac497b59a221257ef441.jpg")

SESSION = getenv("SESSION", "AgBsONl6wdGgTo_hj7wZXLZJZlMn9gXOjkePS7k8vow-8yJK2SAK7rHTmwXT91K9oIz66u_L0NkLkt7HqR3zImVXUtiCQsGeg_HGIkQrS0Q0A2B3GAyy6DKEqBXZz4tK7KV645TBv6ZfHnnFd1mCihHMW3cxaUVw9rv4DDFmnlFGU--gnOJtKG-QKdj9N9T4OxLJVKo46gewb1Ftx5iOQWX5BrqTA6osVDTuanfyKFF5hRE_V0IT2SGWpIYRUgdIB4jjx3pXKWytsJSLuRlgQNVzPwdh72cQ8Bnv3410Novd6rhBQAdlsusSX_NZyoTFeic9xfOLfc_RuquBKe-8DhuiAAAAAVzTqCsA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Behemothicraat")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/HasbullaBlog")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5637445914").split()))


FAILED = "https://telegra.ph/file/9656bed2d9359c9675f52.jpg"
