"""
This python file will scrape the price of the DJM-S5 from DJCity and store it in a variable.
It will also scrape the savings and store it in a variable. 
Finally, it will print the savings and the current price.
"""
# import packages
import requests
from bs4 import BeautifulSoup
import json
import re

# get the price of the DJM-S5 from DJCity
djc = "https://djcity.com.au/product/pioneer-djm-s5-scratch-style-2-channel-performance-dj-mixer/"
djc_page = requests.get(djc)
djc_soup = BeautifulSoup(djc_page.content, 'html.parser')
current_price_djc = djc_soup.find_all('div', class_='online-price')[1].get_text()
savings_djc = djc_soup.find_all('div', class_='online-price')[0].get_text()
print("DJCITY:", current_price_djc[38:-2], current_price_djc[7:32], savings_djc[11:-1])

# get the price of the DJM-S5 from StoreDJ
sdj = "https://www.storedj.com.au/products/pioneer-djms5-scratch-style-2-channel-dj-mixer-for-serato-dj-pro-gloss-red"
sdj_page = requests.get(sdj)
sdj_soup = BeautifulSoup(sdj_page.content, 'html.parser')

# use regex to find the price and savings
sdj_scripts = sdj_soup.find_all('script')
for script in sdj_scripts:
    script_text = script.string
    if script_text:
        price_pattern = r'"price"\s*:\s*\{[^}]*"currencyCode"\s*:\s*"(AUD|[A-Z]+)"[^}]*"amount"\s*:\s*"([^"]+)"'
        match = re.search(price_pattern, script_text)

        if match:
            print("STOREDJ:")
            print(f"Currency Code: {match.group(1)}")
            print(f"Amount: {match.group(2)}")