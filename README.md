# Webscraping
This code fetches the specific samsung phone brand name and their corresponding price in Kenya Shillings
# Jumia Product Price Scraper

This Python script allows you to scrape the prices of Samsung smartphones from the Jumia website. It utilizes the BeautifulSoup library for web scraping and the requests library for making HTTP requests.

## Prerequisites

Before running the script, ensure that you have the following:

- Python programming language installed on your system.
- BeautifulSoup library installed (`pip install beautifulsoup4`).
- Requests library installed (`pip install requests`).

## Usage

1. Set the target URL:
   - Replace the `url` variable with the URL of the Jumia webpage containing the Samsung smartphones.
   - Ensure that the URL is specific to the category you want to scrape (e.g., Samsung smartphones).

2. Run the script:

3. The script will send an HTTP request to the specified URL and scrape the product containers on the page.

4. The prices and names of the Samsung smartphones will be extracted from the product containers and displayed in the console.

## Customization

To customize the script, you can modify the following:

- Target URL: Replace the `url` variable with the URL of the webpage you want to scrape.
- Scraping Logic: Adjust the HTML elements and CSS classes used in the `container.find()` statements to match the structure of the target webpage.
- Data Processing: Modify the way the scraped data is processed or saved according to your requirements.

## Notes

- This script is specific to scraping Samsung smartphone prices from Jumia. To scrape other categories or websites, you will need to adjust the scraping logic accordingly.
- Make sure you comply with the website's terms of service and do not send excessive requests or overload their servers.

## Contributing

Contributions to the project are welcome. If you have any improvements or suggestions, please submit a pull request or open an issue on the repository.
