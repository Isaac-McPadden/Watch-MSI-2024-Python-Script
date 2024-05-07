import webbrowser
from datetime import datetime, timezone
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.util import timedelta
from pytz import utc
# import logging


# Configure logging for people using the .py version and need to use the logger for some reason.  
# Uncomment the import statement above for logger
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Global variables
url = "https://lolesports.com/live/msi/riotgames"
launch_utc_time = datetime.now(timezone.utc)


# Open website function that informs user when function was run
def open_website(url):
    print(f"Attempting to open website at system time {datetime.now()} which is UTC {datetime.now(timezone.utc)}")
    webbrowser.open(url)


# List of specific times in absolute UTC time
specific_times_utc = [
    datetime(2024, 5, 5, 7, 50, tzinfo=timezone.utc),
    datetime(2024, 5, 10, 3, 50, tzinfo=timezone.utc), datetime(2024, 5, 11, 3, 50, tzinfo=timezone.utc),
    datetime(2024, 5, 7, 8, 50, tzinfo=timezone.utc), datetime(2024, 5, 8, 8, 50, tzinfo=timezone.utc), datetime(2024, 5, 9, 8, 50, tzinfo=timezone.utc),
    datetime(2024, 5, 10, 8, 50, tzinfo=timezone.utc), datetime(2024, 5, 12, 8, 50, tzinfo=timezone.utc), datetime(2024, 5, 14, 8, 50, tzinfo=timezone.utc),
    datetime(2024, 5, 15, 8, 50, tzinfo=timezone.utc), datetime(2024, 5, 16, 8, 50, tzinfo=timezone.utc), datetime(2024, 5, 17, 8, 50, tzinfo=timezone.utc),
    datetime(2024, 5, 18, 8, 50, tzinfo=timezone.utc), datetime(2024, 5, 19, 8, 50, tzinfo=timezone.utc)
]


# Initialize the scheduler with UTC timezone
scheduler = BackgroundScheduler(timezone=utc)
scheduler.start()
print('Scheduler initialized with UTC timezone')


# Schedule opening the website at each specific UTC time
for time_utc in specific_times_utc:
    if time_utc > launch_utc_time:
        scheduler.add_job(open_website, 'date', run_date=time_utc, args=[url], misfire_grace_time=60)


# Print the job schedule    
print("Jobs scheduled to run while watch_msi.exe window is open: ")
scheduler.print_jobs()


# Test job to open the website 1 minute from now
test_time_utc = datetime.now(timezone.utc) + timedelta(minutes=1)
scheduler.add_job(open_website, 'date', run_date=test_time_utc, args=[url])
print(f"Test job scheduled to open {url} in 1 minute at {test_time_utc} UTC")


# To keep the script running
try:
    import time
    while True:
        time.sleep(0.5)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()