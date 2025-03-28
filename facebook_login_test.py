from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()  
def test_facebook_login():
    try:
        # Step 1: Open the Facebook login page
        driver.get("https://www.facebook.com/") 
        
        # Step 2: Enter valid email and password
        email_field = driver.find_element(By.ID, "email") 
        password_field = driver.find_element(By.ID, "pass")
        login_button = driver.find_element(By.NAME, "login") 
        
        email_field.send_keys("testuser@fb.com")  
        password_field.send_keys("Fb@1234")  
        
        # Step 3: Click on 'Login'
        login_button.click()
        

        time.sleep(5)
        
        # Step 4: Verify if redirected to the homepage
        expected_url = "https://www.facebook.com/"  
        assert driver.current_url.startswith(expected_url), "Login test failed! User not redirected to homepage."
        print("Test Passed: User successfully logged in.")
    
    except Exception as e:
        print(f"Test Failed: {str(e)}")
    finally:
        driver.quit()

test_facebook_login()
