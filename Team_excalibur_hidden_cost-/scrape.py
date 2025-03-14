from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Replace these with your Amazon credentials
amazon_email = "bangari.sainithin12@gmail.com"
amazon_password = "SAINITHIN@35"

# Initialize Flask app
app = Flask(__name__)

def click_element_with_js(driver, element):
    """Click an element using JavaScript execution."""
    driver.execute_script("arguments[0].scrollIntoView(true);", element)  # Scroll into view
    driver.execute_script("arguments[0].click();", element)  # Click using JavaScript

@app.route('/automate', methods=['GET'])
def automate_amazon_purchase():
    amazon_product_url = request.args.get('url')

    if not amazon_product_url:
        return jsonify({"error": "Product URL not provided"}), 400

    # Configure Chrome options
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # Start in maximized mode
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # Initialize WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Hide Selenium detection
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    try:
        # Step 1: Open product page
        driver.get(amazon_product_url)
        print("✅ Opened Product Page")

        # Step 2: Click 'Buy Now' button
        buy_now_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "buy-now-button"))
        )
        click_element_with_js(driver, buy_now_button)
        print("✅ Clicked Buy Now")

        # Step 3: Login to Amazon
        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "ap_email"))
        )
        email_input.send_keys(amazon_email + Keys.TAB)
        time.sleep(1)
        email_input.send_keys(Keys.ENTER)
        print("✅ Entered Email")

        # Step 4: Enter password
        password_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "ap_password"))
        )
        password_input.send_keys(amazon_password)
        time.sleep(1)

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "signInSubmit"))
        )
        click_element_with_js(driver, login_button)
        print("✅ Entered Password & Clicked Sign In")

        # Step 5: Check for 'Use this address' button
        try:
            use_this_address_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Use this address')]/parent::span/input"))
            )
            click_element_with_js(driver, use_this_address_button)
            print("✅ Clicked 'Use this address'")
            time.sleep(3)
        except Exception:
            print("⚠️ 'Use this address' button not found, moving to next step.")

        # Step 6: Select COD payment method
        #iframes = driver.find_elements(By.TAG_NAME, 'iframe')
        #if iframes:
         #   driver.switch_to.frame(iframes[0])

        #cod_payment_radio = WebDriverWait(driver, 40).until(
         #   EC.element_to_be_clickable((By.XPATH, "//*[contains(@id, 'pp-') and contains(@id, '-162')]//div//div"))
        #)
        #click_element_with_js(driver, cod_payment_radio)
        #print("✅ Selected Cash on Delivery")

        # Switch back to main content
        #driver.switch_to.default_content()

        # Step 7: Click "Use this payment method"
        time.sleep(3)  # Allow time for the page update
        use_this_payment_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='ppw-widgetEvent:SetPaymentPlanSelectContinueEvent']"))
        )
        click_element_with_js(driver, use_this_payment_button)
        print("✅ Clicked 'Use this payment method'")

        # Step 8: Scrape delivery and order total
        time.sleep(5)  # Wait for page to load

        delivery_amount = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#subtotals-marketplace-table > tbody > tr:nth-child(2) > td.a-text-right.aok-nowrap.a-nowrap"))
        ).text

        order_total = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#subtotals-marketplace-table > tbody > tr:nth-child(6) > td.a-color-price.a-size-medium.a-text-right.grand-total-price.aok-nowrap.a-text-bold.a-nowrap"))
        ).text

        print(f"✅ Delivery Amount: {delivery_amount}")
        print(f"✅ Order Total: {order_total}")

        return jsonify({
            "Delivery Amount": delivery_amount,
            "Order Total Amount": order_total
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        #input("Press Enter to close the browser...")  # Keep browser open for debugging
        driver.quit()

# Run Flask app on localhost port 5123
if __name__ == "__main__":
    app.run(debug=True, port=5123)
