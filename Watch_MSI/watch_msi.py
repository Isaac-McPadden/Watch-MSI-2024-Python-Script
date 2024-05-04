import webbrowser
import schedule
import time
from datetime import datetime, timedelta

def open_website():
    url = "https://lolesports.com/live/msi/riotgames"
    webbrowser.open(url)

# Define the list of specific times in absolute UTC time
specific_times_utc = [
    datetime(2024, 5, 5, 7, 50),  # May 5th
    datetime(2024, 5, 10, 3, 50), datetime(2024, 5, 11, 3, 50),  # May 10th and May 11th
    datetime(2024, 5, 7, 8, 50), datetime(2024, 5, 8, 8, 50), datetime(2024, 5, 9, 8, 50),
    datetime(2024, 5, 10, 8, 50), datetime(2024, 5, 12, 8, 50), datetime(2024, 5, 14, 8, 50),
    datetime(2024, 5, 15, 8, 50), datetime(2024, 5, 16, 8, 50), datetime(2024, 5, 17, 8, 50),
    datetime(2024, 5, 18, 8, 50), datetime(2024, 5, 19, 8, 50)  # May 7th - May 19th
]

# Function to convert UTC time to local time using system time's UTC offset
def utc_to_local(utc_dt):
    system_offset = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
    utc_offset = timedelta(seconds=-system_offset)
    return utc_dt + utc_offset

# Schedule opening the website at each specific time adjusted for local time
for time_utc in specific_times_utc:
    time_local = utc_to_local(time_utc)
    schedule.every().day.at(time_local.strftime("%H:%M")).do(open_website)

# Run the scheduler continuously
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute