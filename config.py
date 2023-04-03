from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "27199243"))
API_HASH = getenv("API_HASH", "0e30888407241b7436e460f0361b021c")

BOT_TOKEN = getenv("BOT_TOKEN", "5586550312:AAGoYuRgu062tXk0_3t06Of0InG7NCvFgbk")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5637445914"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/9656bed2d9359c9675f52.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/9656bed2d9359c9675f52.jpg")

SESSION = getenv("SESSION", "AgGfBwsAHqZ_ggDJ04V75kZ4-yaXlurI0udMj6rWqqF2M6ZQyaEDpJpWWk_6lopL9G59gXch11-oPAuYPZzVZDcsT0ziK4Le_xNN_aV8ZuQf2lNf2e-RZbiACE0OgE6aGSYJl1ol193XCqMR4o_KQLV_YTaLWY8WuJ1ymGL1-031tu6TiNkup9Wx8zU8CYV-vd0TuKuVAPNiTSwWgQvM1Uw0CjLcRwPETQGE7IzYHgRmbrIFrwKRJq3kMNc6Rp5pcCmzzqdKkwP-H_HeKzntPfPJcOhW0X62IRbspyryJDBDCFzjoxAcYYsofhqb2jXsaE07_D98hD5ubbZBBE1oIFR2OGCoAwAAAAFM-_4oAQ")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kasbinxeyallari1")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ATO_RESMl")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))


FAILED = "https://telegra.ph/file/9656bed2d9359c9675f52.jpg"
