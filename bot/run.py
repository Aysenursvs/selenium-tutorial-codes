from booking.booking import Booking
import time

booking = Booking()
booking.land_first_page()

# Tarayıcıyı 10 saniye açık tut
time.sleep(10)

# Tarayıcıyı kapat
booking.quit()