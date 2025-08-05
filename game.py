import pandas as pd
import requests
from bs4 import BeautifulSoup

# Step 1: Download the webpage using the requests library
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
response = requests.get(url)
html_data_2 = response.text

# Step 2: Parse the HTML data using BeautifulSoup
soup = BeautifulSoup(html_data_2, 'html.parser')

# Step 3: Extract the table with GameStop Revenue and create a DataFrame
# We use pandas.read_html which is efficient for finding tables.
# We pass the parsed HTML string to it.
tables = pd.read_html(str(soup))

# By inspecting the page, we find the GameStop revenue table is the second table (index 1)
gme_revenue = tables[1]

# Rename the columns as requested
gme_revenue.columns = ['Date', 'Revenue']

# Clean the 'Revenue' column to remove the comma and dollar sign
gme_revenue['Revenue'] = gme_revenue['Revenue'].str.replace(r'[\$,]', '', regex=True)

# Step 4: Display the last five rows of the gme_revenue dataframe
print(gme_revenue.tail())