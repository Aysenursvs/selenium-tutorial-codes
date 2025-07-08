from booking.booking import Booking
import time


with Booking() as bot:
    bot.land_first_page()
    #time.sleep(5)  # Wait for 5 seconds to keep the browser open
    bot.select_location("London")
    time.sleep(5)  # Wait for 5 seconds to keep the browser open




