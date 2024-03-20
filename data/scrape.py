import os
import json
import random
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urlparse

def get_user_agent():
    with open('data/agents.json', 'r') as f:
        agents = json.load(f)
    return random.choice(agents)

def fetch_images(profile_url, folder_name):
    try:
        headers = {
            'User-Agent': get_user_agent(),
        }

        start_time = time.time()
        driver = webdriver.Chrome()
        driver.get(profile_url)

        unique_image_urls = set()

        while time.time() - start_time < 30:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            soup = BeautifulSoup(driver.page_source, 'html.parser')

            images = soup.find_all('img', {'src': True})
            image_urls = [img['src'] for img in images if img['src'].startswith('https://i.pinimg.com/')]

            unique_image_urls.update(image_urls)

        user_image_folder = os.path.join('images', folder_name)
        os.makedirs(user_image_folder, exist_ok=True)

        print("Downloading images...")
        for idx, url in enumerate(unique_image_urls, start=1):
            download_image(url, user_image_folder)
            print(f"[+] Downloading image {idx}/{len(unique_image_urls)}")

    except Exception as e:
        print("An error occurred while fetching Pinterest profile:", e)
    finally:
        driver.quit()

def download_image(image_url, folder_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Error downloading image:", e)
        return

    filename = os.path.join(folder_path, os.path.basename(urlparse(image_url).path))
    if not os.path.exists(filename):
        with open(filename, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Skipping {filename} as it already exists.")
