"""
This python file will contain the scraper class 
used to scrape the price of the DJM-S5 from various 
websites and store it in a variable.
"""
# install packages
try:
    import aiohttp
    import asyncio
    import re
    from bs4 import BeautifulSoup
except ImportError as e:
    print("An error occurred while importing packages:")
    print("pip install -r requirements.txt")
    raise e

class scraper:
    """
    uses beautiful soup to scrape the price and savings of the 
    DJM-S5 from both DJCity and Store DJs
    """

    def __init__(self, url):
        self.url = url

    async def soupify(self):
        """
        takes url as input and returns the page content as 
        a soup object
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                page_content = await response.text()
                soup = BeautifulSoup(page_content, 'html.parser')
                return soup

    async def get_djc_price(self):
        """
        takes djc url as input and returns the current price 
        and savings as a tuple
        """
        # get the page content via soupify method
        djc_content = await self.soupify()
        
        # get the current price and savings from the page content
        current_price_djc = djc_content.find_all('div', 
                                                 class_='online-price')[1].get_text()
        savings_djc = djc_content.find_all('div', 
                                           class_='online-price')[0].get_text()
        return current_price_djc, savings_djc
    
    async def get_sdj_price(self):
        """
        takes sdj url as input and returns the current price
        and savings as a tuple
        """
        # get the page content vis soupify method
        sdj_content = await self.soupify()

        # search for the script tage for price data pattern
        scripts = sdj_content.find_all('script')

        for script in scripts:
            script_text = script.string
            if script_text:
                # look for "price":{"currencyCode":"AUD","amount":"..."}
                price_pattern = r'"price"\s*:\s*\{[^}]*"currencyCode"\s*:\s*"(AUD|[A-Z]+)"[^}]*"amount"\s*:\s*"([^"]+)"'
                match = re.search(price_pattern, script_text)

                if match:
                    currency = match.group(1)
                    amount = match.group(2)
                    return amount, currency
        return None, None
        
    async def get_amz_price(self):
        """
        takes amz url as input and returns the current price as a string
        """
        # get the page content via soupify method
        amz_content = await self.soupify()

        # get the current price from the page content
        current_price_amz = amz_content.find_all('span', 
                                                 class_='a-price-whole')[0].get_text()[:-1]
        return current_price_amz
        