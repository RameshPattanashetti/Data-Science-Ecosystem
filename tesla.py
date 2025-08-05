# # import yfinance as yf
# # from bs4 import BeautifulSoup
# import pandas as pd
# # import requests
# url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.html"
# # Tesla=yf.Ticker('TSLA')
# # Tesla_data=Tesla.history(period="max")
# # print(Tesla_data.head())
# # print(Tesla_data.reset_index(inplace=True))
# # html_data=requests.get(url).text
# # soup=BeautifulSoup(html_data,"html.parser")
# # print(soup.prettify())






# tables = pd.read_html(url)
# tesla_revenue = tables[1]


# tesla_revenue.columns = ['Date', 'Revenue']


# tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace('$', '').str.replace(',', '')


# tesla_revenue.dropna(inplace=True)
# tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


# print(tesla_revenue.head())

import pandas as pd
import requests

# The URL you are trying to scrape
url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue' 

# Add a User-Agent header to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Use requests to get the page content
response = requests.get(url, headers=headers)

# Pass the HTML text to read_html instead of the URL
tables = pd.read_html(response.text)

# The rest of your code...
tesla_revenue = tables[1]
tesla_revenue.columns = ['Date', 'Revenue']
# etc...

print(tesla_revenue.head())