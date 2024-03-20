# Pinterest Image Scraper

A Python tool for scraping images from a Pinterest profile.

## Overview

Pinterest Image Scraper is a Python script that allows users to scrape images from a Pinterest profile. It utilizes web scraping techniques to extract image URLs from the user's Pinterest profile page and downloads the images into a specified folder.

## Features

- Scrapes images from a Pinterest profile
- Downloads images into a folder
- Supports custom user agents for requests
- Easy-to-use command-line interface
- Supports specifying the folder name for image downloads

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies by running:
    ```bash
    pip install requests beautifulsoup4 selenium
    ```
3. Prepare your Pinterest user agents by creating a `agents.json` file in the `data` folder.
4. Run the script with the following command:
    ```bash
    python main.py
    ```
5. Follow the prompts to enter the Pinterest profile link and folder name for image downloads.
6. Sit back and wait for the script to scrape and download the images.

## Requirements

- Python
- `requests`, `beautifulsoup4`, and `selenium` Python libraries

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
