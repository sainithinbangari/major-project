﻿# Chrome Extension 

## Overview

This Chrome extension allows users to scrape product information from e-commerce websites directly from their browser. It utilizes a popup interface for entering the product URL and provides real-time scraping functionality click 👉 [You Tube](https://youtu.be/3X69VkNuC_8?si=QpKvAdOAtILiIn3N).

## Project Link
You can view the project [here](https://drive.google.com/file/d/1U50r-Ailh9SyInWPpGwikTAgF9Acui4y/view?usp=sharing).

## Features

1. Scrapes product information from popular e-commerce platforms such as Flipkart, Amazon, and Meesho.
2. Offers a simple and intuitive user interface with a popup for entering the product URL.
3. Utilizes background scripts for handling scraping requests and communicating with the Flask server.
4. Provides real-time feedback on the product title and MRP through the extension popup.

![image](https://github.com/user-attachments/assets/91ff1c28-0d03-45e2-9ccf-2ea095a64853)


## Installation

1. Clone or download the repository to your local machine.
2. Open Google Chrome and navigate to `chrome://extensions/`.
3. Enable Developer mode by toggling the switch in the top right corner.
4. Click on "Load unpacked" and select the directory containing the extension files.

## Usage

1. Once installed, click on the extension icon in the Chrome toolbar to open the popup.
2. Enter the URL of the product you want to scrape in the input field.
3. Click the "Scrape" button to initiate the scraping process.
4. The extension will display the product title and MRP retrieved from the provided URL in real-time.

## Running Procedure in Chrome

1. Open Google Chrome and navigate to `chrome://extensions/`.
2. Enable Developer mode by toggling the switch in the top right corner.
3. Click on "Load unpacked" and select the directory containing the extension files.
4. The extension will be loaded and accessible from the Chrome toolbar.

## Troubleshooting

- If the extension does not work as expected, ensure that the Flask server is running and accessible at the specified endpoint (`http://localhost:5000/scrape`).
- Check the browser console for any error messages or logs that may indicate issues with the extension.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

