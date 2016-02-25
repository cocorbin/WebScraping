
'''
This Program explores how to use a web-scraper to collect data on a regularly determined schedule
without wasting processing or memory resources.  It collects the weekly PDF release from the chicago police
department, extracts the text elements, and begins parsing the texts.

This is a tutorial file that is not complete.

_author_ : Chase O. Corbin
_date_ : 02/25/2016
_memo_ : Developed for the Colloquium in Practical Computing for Economists; Winter 2016
_place_: University of Chicago
_contact_: cocorbin@uchicago.edu
'''


from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import date, datetime, time
from PyPDF2 import PdfFileReader
import requests

## from bs4 import SoupStrainer
## import pdfquery


f = open('murder-data.txt', 'w')


#### Loop over ever week for the next 5 years

for y in range(2016, 2022):
    for w in range(1, 52):

        x = date.weekday(datetime.now())

        ##### This program will continuously try to scrape the same pdf, which is only updated once a week
        #### This sleep command tells it to check and see if 'today' is a Monday.
        ### If the internal clock does not register monday, it goes to sleep for 12 hours before trying again.

        """
        if (x > 0):
            time.sleep(43200)
            continue
        elif (x == 0):
        """

        ### The first available press release is from the "7th Week"

        if (y == 2016 and w < 7):
            continue
        else:

            url_base= "https://portal.chicagopolice.org/portal/page/portal/ClearPath/News/Crime%20Statistics/1_pdfsam_CompStat%20Public%20"


            #2016%20Week%207.pdf

            url_stub= str(y) + "%20Week%2" + "0" + str(w) + ".pdf"
            url = url_base + url_stub

            ## Save file to local path so the PDF can be edited
            r = requests.get(url, stream=True)
            with open("crime.pdf", 'wb') as fd:
                for chunk in r.iter_content(10):
                    fd.write(chunk)


            ## The file must be translated from the proprietary adobe format in order to be accesible to
            ## standard text or html parsers

            page = open("crime.pdf", 'rb')
            pd = PdfFileReader(page)
            content = pd.getPage(0).extractText().split('\n')
            page.close()
            pdf = urlopen(url)
            soup = BeautifulSoup(pdf)


            '''
            pdf = pdfquery.PDFQuery(soup)
            pdf.doc
            pdf.doc.catalog
            '''

            content2 = str(content)
            content3 = content2.replace(" ", "\n")
            f.write(content3)



        #h = open('homicide-data.txt', 'w')

        '''
        for y in range(2015, 2017):
            for m in ('January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'):

                if (m in ['March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] and y > 2015):
                    continue
                else:
                    year = str(y)
                    month = str(m)
                    date = month+', '+year

                url = "http://homicides.redeyechicago.com/"
                page = urlopen(url)
                soup = BeautifulSoup(page)
                heading = soup.find_all("a", href="csv$")
                print(heading)

        heading = soup.h1
        count = soup.h3
        date = heading.renderContents()
        heading.findAllNext()
        #count = soup.find("div", class= "page-header month-name").find("h3").get_text(strip=True)
            print(head)
        #murders = count.renderContents()

        # count = soup.find("span", text=date).parent.find_next_sibling("h1").parent.find_next_sibling("h3").get_text(strip=True)

        # Build timestamp
        timestamp = str(date)

        # Write timestamp and count of homocides to file
        #h.write(timestamp + ',' + murders + '\n')
         '''

# Done getting data! Close file.
f.close()

