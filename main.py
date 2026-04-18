"""
main runner file to run scraper.py
"""
from src.scraper import scraper

# dictionary of urls to scrape
urls = {
    "djcity": "https://djcity.com.au/product/pioneer-djm-s5-scratch-style-2-channel-performance-dj-mixer/",
    "store_dj": "https://www.storedj.com.au/products/pioneer-djms5-scratch-style-2-channel-dj-mixer-for-serato-dj-pro-gloss-red"
}

# scrape the current prices
try:
    current_price_djc, savings_djc = scraper(urls["djcity"]).get_djc_price()
    amount, currency = scraper(urls["store_dj"]).get_sdj_price()

except Exception as e:
    print("An error occurred while scraping:", e)

# print the results
if __name__ == "__main__":
    print("DJCITY:", current_price_djc[38:-2], current_price_djc[7:32], savings_djc[11:-1])
    print("StoreDJ:", "Current Price is: $", amount, currency)
