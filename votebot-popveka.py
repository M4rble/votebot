from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random

for _ in range(1000):
    try:
        print("Starting iteration", _ + 1)
        # Set up Chrome options to use incognito mode
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        # Set the path to your ChromeDriver
        service = Service('chromedriver')
        service.start()

        driver = webdriver.Chrome(service=service, options=chrome_options)

        # insert website URL
        driver.get('website.url.com')

        # Give the page some time to load
        time.sleep(3)

        # Close any potential cookie notification
        try:
            cookie_button = driver.find_element(By.ID, 'cc-notification-wrapper')
            cookie_button.click()
            time.sleep(1)
        except:
            pass  # If there's no cookie notification, just continue


                # Click on the song with aria-label: song-you-wish-to-vote-for
        first_option_first_poll = driver.find_element(By.XPATH, '//input[@aria-label="song-you-wish-to-vote-for"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", first_option_first_poll)
        time.sleep(0.5)
        first_option_first_poll.click()
        time.sleep(1)

                # if there are multiple polls
                # Click on the song with aria-label: song-you-wish-to-vote-for-2
        first_option_second_poll = driver.find_element(By.XPATH, '//input[@aria-label="song-you-wish-to-vote-for-2"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", first_option_second_poll)
        time.sleep(0.5)
        first_option_second_poll.click()
        time.sleep(1)

        # Scroll the vote button into view and click it
        vote_button = driver.find_element(By.XPATH, '//*[@id="poll-submit-button"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", vote_button)
        time.sleep(0.5)
        vote_button.click()

        # Wait for the vote to be registered
        time.sleep(3)

    except Exception as e:
        print(f"An error occurred in iteration {_ + 1}: {e}")

    finally:
        driver.quit()
        time.sleep(5)

print("Voting script completed.")
