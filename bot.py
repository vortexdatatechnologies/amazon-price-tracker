import time
import re
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(level=logging.INFO)

class PriceTracker:
    def __init__(self, url):
        self.url = url
        self.previous_price = 0.0
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def track_price(self):
        try:
            self.driver.get(self.url)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            title = soup.find(id="productTitle").string.strip()
            price = soup.find(class_="a-price").get_text()
            price = price.replace('\n', '.')

            price_number = re.findall(r'\d+\.\d+', price)
            if price_number:
                current_price = float(price_number[0])
            else:
                logging.error("Price extraction failed.")
                return

            if self.previous_price != 0.0:
                percentage_change = ((current_price - self.previous_price) / self.previous_price) * 100
                logging.info(f"\n{title}\nPrice changed by: {percentage_change:.2f}%")

            if current_price < self.previous_price:
                logging.info(f"Price decreased: {current_price}$")
            elif current_price > self.previous_price:
                logging.info(f"Price increased: {current_price}$")
            else:
                logging.info(f"Price remained unchanged: {current_price}$")

            self.previous_price = current_price

        except Exception as e:
            logging.error(f"An error occurred while tracking the price: {e}")

    def start_tracking(self, sleep_interval):
        while True:
            self.track_price()
            time.sleep(sleep_interval)

def main():
    url = 'https://www.amazon.com/dp/B0BP7F8CBG/'
    sleep_interval = 5  # Wait for 5 sec between each check
    tracker = PriceTracker(url)

    try:
        tracker.start_tracking(sleep_interval)
    except KeyboardInterrupt:
        logging.info("Stopping price tracking...")
    finally:
        tracker.driver.quit()

if __name__ == "__main__":
    main()
