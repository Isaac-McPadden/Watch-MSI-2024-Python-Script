# Watch-MSI-2024-Python-Script
Python script that opens your default web browser to MSI 2024 on the Twitch player 10 minutes before the official stream start.  
I couldn't get the tab scheduler chrome extension to work so this is what I came up with.
I made it into an exe file with "pyinstaller --onefile watch_msi.py" in command line in the python directory.  That may be the way to go actually if you have never opened cmd so it's in the repo.
All it does is open and run the python code.  I have it open the MSI website when you launch it so you know it worked.  It opens a black python box and you just minimize that and it runs in the background.
The watch_msi.exe file is in the dist folder inside the main Watch MSI folder.  The actual code is in watch_msi.py in the main Watch MSI folder if you'd rather run the python code directly.
