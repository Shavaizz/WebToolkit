from website_status import main as webstatus
from website_technology import main as webtech
from website_theme_checker import main as webtheme
import time
webstatus()
webtech()
print("Waiting For API cooldown")
time.sleep(10)
print("Api Refreshed")
webtheme()