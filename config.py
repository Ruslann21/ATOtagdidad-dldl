from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "22007754"))
API_HASH = getenv("API_HASH", "7f0d6b4d928155eda014acdb5a014620")

BOT_TOKEN = getenv("BOT_TOKEN", "6195626321:AAF6wLKo1LDVvOYC1vHaGau1_ybyGJxTPTQ")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5539983698"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/3ac497b59a221257ef441.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/3ac497b59a221257ef441.jpg")

SESSION = getenv("SESSION", "AgBY6qpqC0MBZQpauBfZqZjGsB7VeWrSSRlZxBjE-ABTz1GpPOI4Dr5GxHQ-zQy0SAK5TDq-21Js0qByAtGA7mCuvBiChlwJCgt-HWhn64ab8JSjSHNgvqJqcImsYNA1hjn22S8uqgv4XeXEXRXOowZNykBRN1WdKXfBmTvvtPRFt932Fh2JXlDqJK377BBHPrKuR4NnpI73T6okXlFFnQcFvH9151uDrfR6oxPMuUM-eJSXDtAs-M8u5DPYyLZsftNKRXDthd8XB1VP6iq8uSjMFxJHalz36037OLkSgxCr-zX6IRXu1i75NLisoxvbVy-n6aUED-aI_0L9QRu5DtkpAAAAAVzTqCsA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Behemothicraat")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/HasbullaBlog")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5539983698").split()))


FAILED = "https://telegra.ph/file/9656bed2d9359c9675f52.jpg"
