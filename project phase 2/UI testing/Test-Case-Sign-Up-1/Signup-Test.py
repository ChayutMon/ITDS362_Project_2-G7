from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import unittest
import time

class SignupTest(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test case"""
        # Setup Edge options
        edge_options = Options()
        edge_options.add_argument('--start-maximized')
        
        # Initialize Edge WebDriver
        self.driver = webdriver.Edge(options=edge_options)
        self.wait = WebDriverWait(self.driver, 20)  #wait time
        
        # Test Data
        self.test_data = {
            'url': 'http://45.136.236.146:8081/',
            'username': 'testuser1',
            'email': 'test1@example.com',
            'password': 'Test@123'
        }

    def test_signup_positive(self):
        """
        Test ID: Signup-1A
        Description: Positive test case for user signup
        Priority: High
        """
        try:
            # Step 1: Launch browser and navigate to the application
            self.driver.get(self.test_data['url'])
            time.sleep(2)  # Wait for page to fully load
            print("Step 1 - Browser launched successfully")
            
            # Step 2: Click on Sign up button
            signup_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Button--link')]//span[text()='Sign Up']"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", signup_button)
            time.sleep(1)  # Wait for scrolling
            signup_button.click()
            print("Step 2 - Clicked on Sign up button")
            
            # Wait for the popup form to be visible and fully loaded
            time.sleep(2)  # Wait for popup animation
            
            # Step 3: Fill in the signup form in popup
            # Username field - wait for it to be visible and interactable
            username_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            self.wait.until(
                EC.element_to_be_clickable((By.NAME, "username"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", username_field)
            username_field.clear()
            username_field.send_keys(self.test_data['username'])
            print("Entered username")
            
            # Email field
            email_field = self.wait.until(
                EC.element_to_be_clickable((By.NAME, "email"))
            )
            email_field.clear()
            email_field.send_keys(self.test_data['email'])
            print("Entered email")
            
            # Password field
            password_field = self.wait.until(
                EC.element_to_be_clickable((By.NAME, "password"))
            )
            password_field.clear()
            password_field.send_keys(self.test_data['password'])
            print("Entered password")
            
            # Submit button
            submit_button = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.Button.Button--primary.Button--block[type='submit']")
                )
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            time.sleep(1)  # Wait for scrolling
            submit_button.click()
            print("Step 3 - Filled and submitted signup form")
            
            # Wait for success or redirect
            time.sleep(3)  # Wait for form submission
            try:
                success_message = self.wait.until(
                    EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
                )
                print("Test Result - Pass: User successfully registered")
            except:
                # Check if redirected to home page
                self.wait.until(EC.url_contains("/home"))
                print("Test Result - Pass: User successfully registered and redirected to home page")
            
        except Exception as e:
            print(f"Test Result - Fail: {str(e)}")
            # Take screenshot on failure
            self.driver.save_screenshot(f"signup_failure_{time.strftime('%Y%m%d-%H%M%S')}.png")
            raise
            
    def tearDown(self):
        """Clean up after each test case"""
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    # Create test suite and run tests
    suite = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
    unittest.TextTestRunner(verbosity=2).run(suite)