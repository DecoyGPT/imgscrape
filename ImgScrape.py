import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def extract_images_from_url(url, delay=10, user_agent=None):
    options = Options()
    options.add_argument('--headless')
    if user_agent:
        options.add_argument(f"user-agent={user_agent}")

    print("Launching headless browser to navigate the URL...")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    # Wait for the content to load. Adjust the delay as needed.
    print(f"Waiting for {delay} seconds to ensure content is loaded...")
    time.sleep(delay)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    img_tags = soup.find_all('img')
    print(f"Found {len(img_tags)} image(s) on the page.")
    images = [urljoin(url, img['src']) for img in img_tags if img.has_attr('src')]
    return images

def create_html_with_images(image_list, output_file):
    print("Generating HTML file with the images...")
    with open(output_file, 'w') as f:
        f.write("<html><head><style>img{width: 100px; height: 100px; margin: 10px}</style></head><body>")
        for img_url in image_list:
            f.write(f'<a href="{img_url}" target="_blank"><img src="{img_url}" alt="Image"></a>')
        f.write("</body></html>")
    print(f"HTML file generated as {output_file}")

if __name__ == "__main__":
    url = input("Enter the URL: ")

    # Provide a commonly used user agent
    user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  "Chrome/91.0.4472.124 Safari/537.36")
    
    images = extract_images_from_url(url, user_agent=user_agent)
    
    if images:
        create_html_with_images(images, "output.html")
        print("Check output.html for the images.")
    else:
        print("No images found!")