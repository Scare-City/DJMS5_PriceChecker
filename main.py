"""
main runner file to run scraper.py
"""
import asyncio
import polars as pl
from src.scraper import scraper

# dictionary of urls to scrape
urls = {
    "djcity": "https://djcity.com.au/product/pioneer-djm-s5-scratch-style-2-channel-performance-dj-mixer/",
    "store_dj": "https://www.storedj.com.au/products/pioneer-djms5-scratch-style-2-channel-dj-mixer-for-serato-dj-pro-gloss-red",
    "amazon": "https://www.amazon.com.au/Pioneer-DJ-DJM-S5-Scratch-Style-2-Channel/dp/B0B2RB11SF/ref=pd_ci_mcx_mh_mcx_views_0_title"
}

async def main():
    # scrape the current prices concurrently
    try:
        djc_scraper = scraper(urls["djcity"])
        sdj_scraper = scraper(urls["store_dj"])
        amz_scraper = scraper(urls["amazon"])
        
        results = await asyncio.gather(
            djc_scraper.get_djc_price(),
            sdj_scraper.get_sdj_price(),
            amz_scraper.get_amz_price()
        )
        current_price_djc, savings_djc = results[0]
        amount, currency = results[1]
        current_price_amz = results[2]

    except Exception as e:
        print("An error occurred while scraping:", e)
        return

    # print the results in dataframe
    price_df = pl.DataFrame({
    "Store": ["DJCity", "Store DJ", "Amazon"],
    "Current Price": [current_price_djc[-8:-2], amount, current_price_amz],
    "Original Price": [current_price_djc[26:32], None, None],
    "Savings": [savings_djc[11:-1], None, None],
    "urls": [urls["djcity"], urls["store_dj"], urls["amazon"]]
    })

    print(price_df)

if __name__ == "__main__":
    asyncio.run(main())
