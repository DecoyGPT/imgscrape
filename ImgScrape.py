import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urljoin

def get_full_size_image_url(img_url):
    """
    Convert thumbnail image URL to full size URL based on known patterns.
    Current patterns handled: Shopify's CDN URLs with size information.
    """
    shopify_pattern = re.compile(r'_(\d+x)\.png')
    if shopify_pattern.search(img_url):
        img_url = shopify_pattern.sub('.png', img_url)
    return img_url

def extract_images_from_url(url, delay=10, user_agent=None):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument(f'user-agent={user_agent}')
    
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(delay)  # Let JS-loaded content load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    img_tags = soup.find_all('img')
    print(f"Found {len(img_tags)} image(s) on the page.")
    
    # Get full size image URLs
    images = [get_full_size_image_url(urljoin(url, img['src'])) for img in img_tags if img.has_attr('src')]
    
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
    output_filename = input("Enter the desired output filename (e.g., output.html): ")

    # Provide a commonly used user agent
    user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  "Chrome/91.0.4472.124 Safari/537.36")
    
    images = extract_images_from_url(url, user_agent=user_agent)
    
    if images:
        create_html_with_images(images, output_filename)
        print(f"Check {output_filename} for the images.")
    else:
        print("No images found!")