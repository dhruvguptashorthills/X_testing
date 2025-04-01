import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import os
from dotenv import load_dotenv
load_dotenv()

# Test credentials
USERNAME = os.getenv("X_USERNAME")
PASSWORD = os.getenv("X_PASSWORD")


# Result storage
results = []

class TwitterBot:
    def __init__(self, username, password, sleep_time=3):
        self.username = username
        self.password = password
        self.sleep_time = sleep_time
        self.driver = webdriver.Chrome()

    def login(self):
        """Login to Twitter."""
        self.driver.get("https://twitter.com/login")
        time.sleep(self.sleep_time)
        
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        username_field.send_keys(self.username)
        username_field.send_keys(Keys.RETURN)
        
        time.sleep(self.sleep_time)
        
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)
        
        time.sleep(self.sleep_time)
        return "Home" in self.driver.title

    def search(self, search_term):
        """Perform a search and return if results appear."""
        self.driver.get("https://x.com/explore")
        time.sleep(self.sleep_time)
        search_bar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@data-testid="SearchBox_Search_Input"]'))
        )
        search_bar.clear()
        search_bar.send_keys(search_term)
        search_bar.send_keys(Keys.RETURN)
        
        time.sleep(self.sleep_time)
        
        try:
            no_results_message = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "No results")]'))
            )
            return False
        except:
            return True

    def go_to_profile(self):
        """Navigate to user profile."""
        self.driver.get("https://twitter.com/home")
        time.sleep(self.sleep_time)
        profile_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-testid="AppTabBar_Profile_Link"]'))
        )
        profile_link.click()
        time.sleep(self.sleep_time)
        return self.username.lower()[1:] in self.driver.current_url.lower()

    def post_tweet(self, message):
        self.driver.get("https://twitter.com/home")
        time.sleep(self.sleep_time)
        tweet_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-testid="tweetTextarea_0"]'))
        )
        tweet_box.click()
        tweet_box.send_keys(message)
        
        post_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@data-testid="tweetButtonInline"]'))
        )
        # Check if button is disabled (for over-limit tweets)
        if "r-1h3ijdo" in post_button.get_attribute("class"):  # Disabled button class
            return False
        
        post_button.click()
        time.sleep(self.sleep_time)
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, f'//span[contains(text(), "{message}")]'))
            )
            return True
        except:
            return False

    def follow_user(self, username):
        """Follow a specific user."""
        self.driver.get(f"https://twitter.com/{username}")
        time.sleep(self.sleep_time)
        
        follow_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="placementTracking"]//span[contains(text(), "Follow")]'))
        )
        follow_button.click()
        time.sleep(self.sleep_time)
        
        return "Following" in self.driver.page_source
    
    def go_to_home(self):
        """Navigate to Home page via navigation bar."""
        home_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-testid="AppTabBar_Home_Link"]'))
        )
        home_link.click()
        time.sleep(self.sleep_time)
        return "Home" in self.driver.title

    def go_to_explore(self):
        """Navigate to Explore page via navigation bar."""
        explore_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-testid="AppTabBar_Explore_Link"]'))
        )
        explore_link.click()
        time.sleep(self.sleep_time)
        return "explore" in self.driver.current_url

    def go_to_notifications(self):
        """Navigate to Notifications page via navigation bar."""
        notifications_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-testid="AppTabBar_Notifications_Link"]'))
        )
        notifications_link.click()
        time.sleep(self.sleep_time)
        return "notifications" in self.driver.current_url

    def go_to_messages(self):
        """Navigate to Messages page via navigation bar."""
        messages_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-testid="AppTabBar_DirectMessage_Link"]'))
        )
        messages_link.click()
        time.sleep(self.sleep_time)
        return "messages" in self.driver.current_url
    def check_grok(self):
        grok_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Grok"]'))
        )
        grok_link.click()
        time.sleep(self.sleep_time)
        return "grok" in self.driver.current_url
    def check_bookmarks(self):
        bookmark_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Bookmarks"]'))
        )
        bookmark_link.click()
        time.sleep(self.sleep_time)
        return "bookmarks" in self.driver.current_url

    def check_communities(self):
        communities_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Communities"]'))
        )
        communities_link.click()
        time.sleep(self.sleep_time)
        return "communities" in self.driver.current_url
    def check_premium(self):
        premium_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Premium"]'))
        )
        premium_link.click()
        time.sleep(self.sleep_time)
        return "premium" in self.driver.current_url

    def check_verified_org_status(self):
        self.driver.get(f"https://twitter.com/{self.username[1:]}")
        time.sleep(self.sleep_time)
        try:
            gold_check = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//svg[contains(@data-testid, "icon-verified-org")]'))
            )
            return gold_check.is_displayed()
        except:
            return False
    def cleanup(self):
        """Close the browser."""
        time.sleep(self.sleep_time)
        self.driver.quit()

# Helper function to log results and save to CSV
def log_result(test_id, test_name, description, outcome):
    result = [test_id, test_name, description, outcome]
    results.append(result)
    print(f"Recorded result: {result}")  # Debug statement

    # Append result to CSV file immediately
    csv_file = "test_results.csv"
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:  # Write header if file doesn't exist
            writer.writerow(["Test ID", "Test Case Name", "Description", "Result"])
        writer.writerow(result)

# Pytest fixtures and hooks
@pytest.fixture(scope="session")
def twitter_bot():
    """Fixture to set up TwitterBot, log in once, and tear down after all tests."""
    bot = TwitterBot(USERNAME, PASSWORD, sleep_time=3)
    assert bot.login(), "Initial login failed"
    yield bot
    bot.cleanup()

# Ensure results are finalized before closing the driver
@pytest.fixture(scope="session", autouse=True)
def finalize_results():
    yield  # Wait for all tests to complete
    print("\nAll tests completed. Results are stored in test_results.csv.")

# Test cases
def test_search_functionality(twitter_bot):
    test_id = "TC001"
    description = "Test if search returns relevant results"
    search_term = "python programming"
    try:
        assert twitter_bot.search(search_term) == True, f"Search for '{search_term}' failed"
        log_result(test_id, "test_search_functionality", description, "Passed")
    except AssertionError as e:
        log_result(test_id, "test_search_functionality", description, "Failed")
        raise e

def test_search_empty_results(twitter_bot):
    test_id = "TC002"
    description = "Test search with a nonsense term"
    search_term = "asdkfjhas112121212121dkfjh"
    try:
        assert twitter_bot.search(search_term) == False, "Search returned results for nonsense term"
        log_result(test_id, "test_search_empty_results", description, "Passed")
    except AssertionError as e:
        log_result(test_id, "test_search_empty_results", description, "Failed")
        raise e

def test_profile_navigation(twitter_bot):
    test_id = "TC003"
    description = "Test navigation to user profile"
    try:
        assert twitter_bot.go_to_profile() == True, "Failed to navigate to profile"
        log_result(test_id, "test_profile_navigation", description, "Passed")
    except AssertionError as e:
        log_result(test_id, "test_profile_navigation", description, "Failed")
        raise e

def test_page_load_time(twitter_bot):
    test_id = "TC004"
    description = "Test if search page loads within acceptable time"
    start_time = time.time()
    twitter_bot.search("test")
    end_time = time.time()
    try:
        assert (end_time - start_time) < 15, "Search page load took too long (>10s)"
        log_result(test_id, "test_page_load_time", description, "Passed")
    except AssertionError as e:
        log_result(test_id, "test_page_load_time", description, "Failed")
        raise e

def test_post_tweet(twitter_bot):
    test_id = "TC005"
    description = "Test posting a tweet"
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    test_message = f"Test tweet from bot {timestamp}"
    try:
        assert twitter_bot.post_tweet(test_message) == True, "Failed to post tweet"
        log_result(test_id, "test_post_tweet", description, "Passed")
    except AssertionError as e:
        log_result(test_id, "test_post_tweet", description, "Failed")
        raise e

def test_follow_user(twitter_bot):
    test_id = "TC006"
    description = "Test following a user"
    test_user = "PMOIndia"
    try:
        assert twitter_bot.follow_user(test_user) == True, f"Failed to follow {test_user}"
        log_result(test_id, "test_follow_user", description, "Passed")
    except AssertionError as e:
        log_result(test_id, "test_follow_user", description, "Failed")
        raise e

def test_tweet_character_limit(twitter_bot):
    test_id = "TC007"
    description = "Test posting a tweet exceeding character limit"
    long_message = "a" * 283
    try:
        assert twitter_bot.post_tweet(long_message) == False, "Successfully posted tweet exceeding character limit"
        log_result(test_id, "test_tweet_character_limit", description, "Passed")
    except AssertionError as e:
        log_result(test_id, "test_tweet_character_limit", description, "Failed")
        raise e

@pytest.mark.parametrize("hashtag", ["#AI"])
def test_hashtag_search(twitter_bot, hashtag):
    test_id = "TC008"
    description = "Test searching with hashtags"
    try:
        assert twitter_bot.search(hashtag) == True, f"Hashtag search failed for {hashtag}"
        log_result(test_id, "test_hashtag_search", description, "Passed")
    except AssertionError as e:
        log_result(test_id, "test_hashtag_search", description, "Failed")
        raise e

def test_profile_not_found(twitter_bot):
    test_id = "TC009"
    description = "Test navigating to non-existent profile"
    invalid_user = "nonexistentuser123456789"
    twitter_bot.driver.get(f"https://twitter.com/{invalid_user}")
    time.sleep(twitter_bot.sleep_time)
    try:
        error_message = WebDriverWait(twitter_bot.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "This account doesn’t exist")]'))
        )
        assert error_message.is_displayed(), "Did not detect non-existent profile"
        log_result(test_id, "test_profile_not_found", description, "Passed")
    except AssertionError as e:
        log_result(test_id, "test_profile_not_found", description, "Failed")
        raise e

def test_home_navigation(twitter_bot):
    test_id = "TC010"
    description = "Test navigation to Home page via nav bar"
    try:
        twitter_bot.go_to_profile()
        assert twitter_bot.go_to_home() == True, "Failed to navigate to Home page"
        log_result(test_id, "test_home_navigation", description, "Passed")
    except AssertionError as e:
        log_result(test_id, "test_home_navigation", description, "Failed")
        raise e

def test_explore_navigation(twitter_bot):
    test_id = "TC011"
    description = "Test navigation to Explore page via nav bar"
    try:
        twitter_bot.go_to_home()
        assert twitter_bot.go_to_explore() == True, "Failed to navigate to Explore page"
        log_result(test_id, "test_explore_navigation", description, "Passed")
    except AssertionError as e:
        log_result(test_id, "test_explore_navigation", description, "Failed")
        raise e

def test_notifications_navigation(twitter_bot):
    test_id = "TC012"
    description = "Test navigation to Notifications page via nav bar"
    try:
        twitter_bot.go_to_home()
        assert twitter_bot.go_to_notifications() == True, "Failed to navigate to Notifications page"
        log_result(test_id, "test_notifications_navigation", description, "Passed")
    except AssertionError as e:
        log_result(test_id, "test_notifications_navigation", description, "Failed")
        raise e

def test_messages_navigation(twitter_bot):
    test_id = "TC013"
    description = "Test navigation to Messages page via nav bar"
    try:
        twitter_bot.go_to_home()
        assert twitter_bot.go_to_messages() == True, "Failed to navigate to Messages page"
        log_result(test_id, "test_messages_navigation", description, "Passed")
    except AssertionError as e:
        log_result(test_id, "test_messages_navigation", description, "Failed")
        raise e

def test_grok(twitter_bot):
    test_id = "TC014"
    description = "Test if Grok option is clickable in the More menu"
    try:
        assert twitter_bot.check_grok() == True, "Grok option is not clickable"
        log_result(test_id, "test_grok", description, "Passed")
    except AssertionError as e:
        log_result(test_id, "test_grok", description, "Failed")
        raise e

def test_bookmarks(twitter_bot):
    test_id = "TC015"
    description = "Test if Bookmarks option is clickable in the More menu"
    try:
        assert twitter_bot.check_bookmarks() == True, "Bookmarks option is not clickable"
        log_result(test_id, "test_bookmarks", description, "Passed")
    except AssertionError as e:
        log_result(test_id, "test_bookmarks", description, "Failed")
        raise e

def test_communities(twitter_bot):
    test_id = "TC016"
    description = "Test if Communities option is clickable in the More menu"
    try:
        assert twitter_bot.check_communities() == True, "Communities option is not clickable"
        log_result(test_id, "test_communities", description, "Passed")
    except AssertionError as e:
        log_result(test_id, "test_communities", description, "Failed")
        raise e

def test_premium(twitter_bot):
    test_id = "TC017"
    description = "Test if Premium option is clickable in the More menu"
    try:
        assert twitter_bot.check_premium() == True, "Premium option is not clickable"
        log_result(test_id, "test_premium", description, "Passed")
    except AssertionError as e:
        log_result(test_id, "test_premium", description, "Failed")
        raise e

def test_verified_org_status(twitter_bot):
    test_id = "TC018"
    description = "Test if account has Verified Organization status"
    try:
        result = twitter_bot.check_verified_org_status()
        print(f"Verified Org Status: {result}")
        log_result(test_id, "test_verified_org_status", description, "Passed" if result else "Failed")
    except AssertionError as e:
        log_result(test_id, "test_verified_org_status", description, "Failed")
        raise e

if __name__ == "__main__":
    pytest.main(["-v"])