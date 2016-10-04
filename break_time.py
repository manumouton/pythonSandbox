import webbrowser
import time


print("This program started at " + time.ctime())

total_breaks = 3
time_between_breaks = 2*60*60

for i in range(0,total_breaks):
    # Wait for a few seconds
    time.sleep(time_between_breaks)
    # Open the browser in the given url
    webbrowser.open("http://www.google.lu")


