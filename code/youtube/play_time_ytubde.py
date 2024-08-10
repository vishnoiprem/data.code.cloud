from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Specify the path to your Brave browser
brave_path = '/Users/vishnoiprem/Applications/BraveBrowser.app/Contents/MacOS/Brave Browser'

# Specify the path to the ChromeDriver
chrome_driver_path = '/Users/vishnoiprem/Applications/to/chromedriver'  # Replace with your actual path

# Set up the options to use Brave
options = webdriver.ChromeOptions()
options.binary_location = brave_path

# Set up the ChromeDriver service
service = Service(executable_path=chrome_driver_path)

# Create a new Brave session
driver = webdriver.Chrome(service=service, options=options)

# Navigate to YouTube
driver.get("https://www.youtube.com")

# Allow time for the page to load
time.sleep(3)

# Find the search box using its name attribute value
search_box = driver.find_element("name", "search_query")

# Enter your search term
search_box.send_keys("cloudvala")

# Press the Enter key to start the search
search_box.send_keys(Keys.RETURN)

# Allow time for search results to load
time.sleep(3)

# Click on the first video in the search results
video = driver.find_element("id", "video-title")
video.click()

# Let the video play for a specific duration or until the end
time.sleep(60)  # This will keep the video playing for 60 seconds

# Close the browser window
driver.quit()
