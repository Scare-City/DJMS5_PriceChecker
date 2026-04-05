"""
This python file will scrape the price of the DJM-S5 from DJCity and store it in a variable.
It will also scrape the savings and store it in a variable. 
Finally, it will print the savings and the current price.
"""
# import packages
import requests
from bs4 import BeautifulSoup

# get the price of the DJM-S5 from DJCity
djc = "https://djcity.com.au/product/pioneer-djm-s5-scratch-style-2-channel-performance-dj-mixer/"
djc_page = requests.get(djc)
soup = BeautifulSoup(djc_page.content, 'html.parser')
current_price_djc = soup.find_all('div', class_='online-price')[1].get_text()
savings_djc = soup.find_all('div', class_='online-price')[0].get_text()
print("DJCITY:", current_price_djc[38:-2], current_price_djc[7:32], savings_djc[11:-1])