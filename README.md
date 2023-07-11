# Amazon Price Tracker
This project is an automated price tracker that is used to track changes in the price of a product on Amazon. It uses web scraping with Selenium and Beautiful Soup to collect the data and then calculates the percentage change in price.
## Features
- Retrieves the product title and price from the provided Amazon URL.
- Uses regular expressions to extract the numeric value of the price.
- Tracks the price changes and calculates the percentage change compared to the previous price.
- Notifies the user when the price decreases or increases.
- Runs continuously, checking the price at regular intervals.
- Implemented with Python, Selenium, and ChromeDriverManager.
## How to Use
1. ***pip install -r requirements.txt***
2. Enter in line 54 the URL of the product you want to track.
![Screenshot_1](https://github.com/vortexdatatechnologies/amazon-price-tracker/assets/139167026/17e581b6-dbba-41c7-91c1-6565b8b98bec)
3. Enter in line 55 the number of seconds you want to wait between each request
![Screenshot_200](https://github.com/vortexdatatechnologies/amazon-price-tracker/assets/139167026/b371ace5-64a5-4498-998b-dabf1e142444)
4. ***python bot.py***
5. It's ready
![Screenshot_201](https://github.com/vortexdatatechnologies/amazon-price-tracker/assets/139167026/e852eb61-fad7-4eb4-8c73-1ba6b5b97e21)
## Warning
This project is intended for educational purposes and should not be used for large-scale scraping on Amazon or any other website, as this may be against their Terms of Service. Please be sure to use it responsibly.
Also, the code is configured to use the Chrome browser. If you wish to use another browser, you will need to adjust your WebDriver settings accordingly.
