'''
This Program explores how to use a web-scraper to collect archived (historical) data from a popular weather
service. It collects the daily temperature (taken as the average between observed high and low) as well
as the average monthly temperature as calculated on the 25th of every month. It outputs two CSV files, each
with two columns, corresponding to the date and temperature.

This script is complete (but needs to be made faster.)

For additional resources, please see:

"https://www.wunderground.com/weather/api/d/docs?d=resources/code-samples"

_author_ : Chase O. Corbin
_date_ : 02/25/2016
_memo_ : Developed for the Colloquium in Practical Computing for Economists; Winter 2016
_place_: University of Chicago
_contact_: cocorbin@uchicago.edu
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import time, timedelta, tzinfo
import csv

## import requests
## import time


with open('weather-data-monthly.csv', 'w') as monthlyFile:
    cols = ['Month ', ' Average']
    writer = csv.DictWriter(monthlyFile, fieldnames=cols)

    writer.writeheader()

    # Iterate through year, month, and day
    for y in range(2001, 2017):
        for m in range(1, 13):

            '''
            for d in range(31, 27, -1):
            if (m == 2 and d > 28):
                continue
            elif (m in [4, 6, 9, 10] and d > 30):
                continue
            '''

            if (y == 2016 and m > 2):
                continue

            # Open wunderground.com url
            url1 = "http://www.wunderground.com/history/airport/KMDW/" + str(y) + "/" + str(m) + "/" + "24" + "/MonthlyHistory.html"
            page1 = urlopen(url1)

            # Get temperature from page
            soup1 = BeautifulSoup(page1)
            mTemp = soup1.find("span", text="Mean Temperature").parent.find_next_sibling("td").get_text(strip=True)
            monthlyTemp = mTemp.replace("°F", "")


            # Format month for timestamp
            if len(str(m)) < 2:
                mStamp = '0' + str(m)
            else:
                mStamp = str(m)

            '''
            # Format day for timestamp
            if len(str(d)) < 2:
            dStamp = '0' + str(d)
            else:
            dStamp = str(d)
            '''

            yStamp = str(y)

            temps = "The average temperature during"
            today = mStamp + "," + yStamp
            print(temps + " " + today + " " + "was" + " " + mTemp)

            # Build timestamp
            # timestamp =  mStamp + '/' + dStamp + '/'  + str(y)

            monthstamp = mStamp + '-' + str(y)

            # Write timestamp and temperature to file
            # f1.write(timestamp + ',' + dailyTemp + '\n')

            writer.writerow({'Month ': monthstamp, ' Average': monthlyTemp})

            time.sleep(0.5)
        time.sleep(0.5)
    time.sleep(0.5)

# Done getting monthly data! Close file.
monthlyFile.close()

# Go to sleep before starting daily temperature collection
time.sleep(2.5)

# Create/open a file called wunder.txt (which will be a comma-delimited file)
with open('weather-data-daily.csv', 'w') as dailyFile:
    cols = ['Date ', ' Temp']
    writer = csv.DictWriter(dailyFile, fieldnames=cols)

    writer.writeheader()

    # Iterate through year, month, and day
    for y in range(2001, 2017):
        for m in range(1, 13):
            for d in range(1, 32):

                # Check if already gone through month
                if (m == 2 and d > 28):
                    continue
                elif (m in [4, 6, 9, 11] and d > 30):
                    continue
                if (y == 2016 and m > 2):
                    continue

                # Open wunderground.com url
                url2 = "http://www.wunderground.com/history/airport/KMDW/" + str(y) + "/" + str(m) + "/" + str(d) + "/DailyHistory.html"
                page2 = urlopen(url2)

                # Get temperature from page
                soup2 = BeautifulSoup(page2)
                dTemp = soup2.find("span", text="Mean Temperature").parent.find_next_sibling("td").get_text(strip=True)
                dailyTemp = dTemp.replace("°F", "")

                # Format month for timestamp
                if len(str(m)) < 2:
                    mStamp = '0' + str(m)
                else:
                    mStamp = str(m)

                # Format day for timestamp
                if len(str(d)) < 2:
                    dStamp = '0' + str(d)
                else:
                    dStamp = str(d)

                yStamp = str(y)

                # Print statement to check if everything is working
                temps = "The temperature on"
                today = mStamp + "-" + dStamp + "-" + yStamp
                print(temps + " " + today + " " + "was" + " " + dTemp)

                # Build timestamp
                timestamp = mStamp + '-' + dStamp + '-' + str(y)
                monthstamp = mStamp + '-' + str(y)

                writer.writerow({'Date ': timestamp, ' Temp': dailyTemp})

                time.sleep(0.5)
        time.sleep(0.5)
    time.sleep(0.5)

# Done getting daily data! Close file.
dailyFile.close()



