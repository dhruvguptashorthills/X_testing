# Twitter Automation and Testing Framework

This project is a Python-based automation framework for testing various functionalities of Twitter using Selenium WebDriver and Pytest. It includes automated test cases for login, navigation, posting tweets, searching, and interacting with tweets (like, comment, retweet, bookmark).

## Features

- Automated login to Twitter.
- Test cases for:
  - Searching tweets.
  - Navigating to profile, home, explore, notifications, and messages.
  - Posting tweets and validating character limits.
  - Following users.
  - Liking, commenting, retweeting, and bookmarking tweets.
  - Checking additional features like Grok, Communities, Premium, and Verified Organization status.
- Results are logged into a CSV file (`test_results.csv`).

## Prerequisites

- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Required Python packages:
  - `selenium`
  - `pytest`

## Setup Instructions

1. Clone this repository or download the code.
2. Install the required Python packages:
   ```bash
   pip install selenium pytest
   ```
3. Download ChromeDriver and ensure it is in your system's PATH or the same directory as the script.
4. Update the `USERNAME` and `PASSWORD` variables in `app.py` with valid Twitter credentials.

## Running the Tests

1. Navigate to the project directory:
   ```bash
   cd /home/shtlp_0152/Desktop/Assignments/QA Task
   ```
2. Run the tests using Pytest:
   ```bash
   pytest -v
   ```
3. Test results will be displayed in the terminal and logged into `test_results.csv`.

## File Structure

- `app.py`: Main script containing the `TwitterBot` class and test cases.
- `test_results.csv`: CSV file where test results are logged.

## Test Cases

| Test ID | Test Case Name               | Description                                      |
|---------|------------------------------|--------------------------------------------------|
| TC001   | test_search_functionality    | Test if search returns relevant results         |
| TC002   | test_search_empty_results    | Test search with a nonsense term                |
| TC003   | test_profile_navigation      | Test navigation to user profile                 |
| TC004   | test_page_load_time          | Test if search page loads within acceptable time|
| TC005   | test_post_tweet              | Test posting a tweet                            |
| TC006   | test_follow_user             | Test following a user                           |
| TC007   | test_tweet_character_limit   | Test posting a tweet exceeding character limit  |
| TC008   | test_hashtag_search          | Test searching with hashtags                    |
| TC009   | test_profile_not_found       | Test navigating to non-existent profile         |
| TC010   | test_home_navigation         | Test navigation to Home page via nav bar        |
|....  | ....    | .....   |


## Notes

- Ensure that the Twitter account used for testing has the necessary permissions and is not restricted.
- Use a test account to avoid violating Twitter's terms of service.
- The script is designed for educational purposes and should not be used for spamming or malicious activities.

## License

This project is licensed under the MIT License. See the LICENSE file for details.