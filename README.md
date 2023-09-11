## ImgScrape

`ImgScrape` is a Python script that extracts all image URLs from a given web page. It captures both statically-loaded and dynamically-loaded images, ensuring comprehensive coverage of a page's visual content.

### Features:

- Scans both statically-loaded and dynamically-loaded images.
- Converts known thumbnail URLs (e.g., from Shopify) to full-sized image URLs when possible.
- Provides console feedback for a transparent user experience.
- Generates an HTML file with previews of the retrieved images.
- User-friendly: simply input the URL you want to scrape and your desired output filename.

### Dependencies:

- `beautifulsoup4`: For parsing the webpage.
- `selenium`: To handle pages with dynamically loaded content.
- ChromeDriver: An executable needed by Selenium to control the Google Chrome browser.

### Installation:

1. Clone the repository:
   ```sh
   git clone https://github.com/DecoyGPT/ImgScrape.git
   ```

2. Change to the cloned directory:
   ```sh
   cd ImgScrape
   ```

3. Install the required Python packages:
   ```sh
   pip install beautifulsoup4 selenium
   ```

4. Download the [ChromeDriver executable](https://sites.google.com/a/chromium.org/chromedriver/) and place it in the same directory as the script or make sure it's in your system's PATH.

### Usage:

1. Execute the script:
   ```sh
   python ImgScrape.py
   ```

2. When prompted, input the website URL and your desired output filename.

3. The script will navigate the page, retrieve images, and generate an HTML file with the specified name.

4. Review the generated HTML file in the project directory to see the images.

### Disclaimer:

Use this tool responsibly and ethically. Avoid scraping websites without permission and always heed the `robots.txt` file of any website.
