# Watch-MSI-2024-Python-Script
Executable Python script that opens your default web browser to MSI 2024 on the Twitch player 10 minutes before the official stream start.  
I couldn't get the tab scheduler chrome extension to work so this is what I came up with.
I made it into an exe file with "pyinstaller --onefile watch_msi.py" in command line in the python directory.  The .py file is in there if you have a python environment and prefer to run it that way.
All it does is open and run the python code down below.  I have it open the MSI website a minute after you launch it so you know if it works.  It opens a black python box and you just minimize that and it runs in the background.
The watch_msi.exe file is in the dist folder inside the main Watch MSI folder.  The actual code is in watch_msi.py in the main Watch MSI folder if you'd rather run the python code directly.
You may have to whitelist it with your antivirus.


Python code that is run:

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
        scheduler.add_job(open_website, 'date', run_date=time_utc, args=[url])


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
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
