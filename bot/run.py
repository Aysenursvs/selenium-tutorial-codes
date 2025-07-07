from booking.booking import Booking
import time


with Booking() as bot:
    bot.land_first_page()
    time.sleep(10)  # Wait for 10 seconds to keep the browser open
    print("Exiting...")

# Tarayıcıyı 10 saniye açık tut



