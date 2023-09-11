## ImgScrape

`ImgScrape` is a simple Python script that allows users to extract all image URLs from a given web page. Using both BeautifulSoup and Selenium, it handles static and JavaScript-loaded images, ensuring a comprehensive scan of the page's visual content.

### Features:

- Scans for both statically-loaded and dynamically-loaded images.
- Provides console feedback for better user interaction.
- Generates an HTML file with previews of found images.
- User-friendly: just input the URL you want to scrape.

### Dependencies:

- `beautifulsoup4`: For parsing the webpage.
- `selenium`: To render pages and handle dynamically loaded content.
- ChromeDriver: An executable required by Selenium to interact with the Google Chrome browser.

### Installation:

1. Clone the repository:
   ```sh
   git clone https://github.com/DecoyGPT/ImgScrape.git
   ```

2. Navigate to the cloned directory:
   ```sh
   cd ImgScrape
   ```

3. Install the required Python libraries:
   ```sh
   pip install beautifulsoup4 selenium
   ```

4. Download the [ChromeDriver executable](https://sites.google.com/a/chromium.org/chromedriver/) and place it in the same directory as the script, or ensure it's available in your system's PATH.

### Usage:

1. Run the script:
   ```sh
   python ImgScrape.py
   ```

2. Enter the desired URL when prompted.

3. Wait for the script to navigate the page, extract images, and generate an output HTML file.

4. Check the generated `output.html` in the project directory to view the images.

### Disclaimer:

Please use this tool responsibly and ethically. Do not scrape websites without permission, and always respect the `robots.txt` of any site.
