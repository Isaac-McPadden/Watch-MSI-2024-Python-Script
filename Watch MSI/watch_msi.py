import webbrowser
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def open_website(url):
    webbrowser.open(url)

# List of specific times in absolute UTC time
specific_times_utc = [
    datetime(2024, 5, 5, 7, 50),
    datetime(2024, 5, 10, 3, 50), datetime(2024, 5, 11, 3, 50),
    datetime(2024, 5, 7, 8, 50), datetime(2024, 5, 8, 8, 50), datetime(2024, 5, 9, 8, 50),
    datetime(2024, 5, 10, 8, 50), datetime(2024, 5, 12, 8, 50), datetime(2024, 5, 14, 8, 50),
    datetime(2024, 5, 15, 8, 50), datetime(2024, 5, 16, 8, 50), datetime(2024, 5, 17, 8, 50),
    datetime(2024, 5, 18, 8, 50), datetime(2024, 5, 19, 8, 50)
]

url = "https://lolesports.com/live/msi/riotgames"

# Initialize the scheduler
scheduler = BackgroundScheduler()
scheduler.start()

# Schedule opening the website at each specific UTC time
for time_utc in specific_times_utc:
    scheduler.add_job(open_website, 'date', run_date=time_utc, args=[url])

# Open website once when the code is initialized
open_website(url)

# To keep the script running
try:
    import time
    while True:
        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()