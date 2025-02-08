from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from concurrent.futures import ThreadPoolExecutor
import sys


def setup_driver():
    """Setup and return configured webdriver"""
    try:
        # Configure Safari options
        options = webdriver.SafariOptions()
        driver = webdriver.Safari(options=options)
        return driver
    except Exception as e:
        print(f"Error setting up Safari driver: {str(e)}")
        print("\nPlease ensure you have:")
        print("1. Enabled 'Allow Remote Automation' in Safari's Develop menu")
        print("2. Enabled the Develop menu in Safari > Preferences > Advanced")
        sys.exit(1)


def play_video(url, duration):
    """
    Play a single video for specified duration
    """
    driver = None
    try:
        print(f"Starting playback of {url}")
        driver = setup_driver()
        driver.get(url)

        # Wait for and click play button
        play_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ytp-play-button"))
        )
        play_button.click()

        # Let video play for specified duration
        time.sleep(duration)

    except Exception as e:
        print(f"Error playing video {url}: {str(e)}")
    finally:
        if driver:
            try:
                driver.quit()
            except Exception as e:
                print(f"Error closing driver: {str(e)}")


def main():
    # List of video URLs
    video_urls = [
        "https://www.youtube.com/watch?v=SPX73_-4JfY",
        "https://www.youtube.com/watch?v=0GdHazY_YNQ",
        # Add more URLs
    ]

    # Settings
    hours_per_video = 1
    seconds_per_video = hours_per_video * 3600
    max_concurrent = 2  # Reduced for testing

    print("Starting video playback script...")
    print(f"Maximum concurrent videos: {max_concurrent}")
    print("Please ensure Safari's 'Allow Remote Automation' is enabled\n")

    with ThreadPoolExecutor(max_workers=max_concurrent) as executor:
        while True:
            try:
                random.shuffle(video_urls)
                futures = [
                    executor.submit(play_video, url, seconds_per_video)
                    for url in video_urls[:max_concurrent]
                ]

                for future in futures:
                    try:
                        future.result()
                    except Exception as e:
                        print(f"Error in thread execution: {str(e)}")

            except KeyboardInterrupt:
                print("\nStopping script...")
                break
            except Exception as e:
                print(f"Error in main loop: {str(e)}")
                time.sleep(5)  # Wait before retrying


if __name__ == "__main__":
    main()