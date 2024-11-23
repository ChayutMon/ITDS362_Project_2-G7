from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import unittest
import time

class SignupTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test environment before the test suite"""
        print("Initializing WebDriver...")
        edge_options = Options()
        edge_options.add_argument('--start-maximized')
        cls.driver = webdriver.Edge(options=edge_options)
        cls.wait = WebDriverWait(cls.driver, 20)  # Shared wait object

    def setUp(self):
        """Test data and reset the browser state before each test"""
        self.test_data = {
            'url': 'http://45.136.236.146:8081/',
            'username': 'testuser19',
            'email': 'test19@example.com',
            'password': 'Test@123',
        }
        print("Navigating to application URL...")
        self.driver.get(self.test_data['url'])

    def test_signup_positive(self):
        """Positive test case for user signup"""
        print("Starting test: test_signup_positive")
        try:
            # Step 1: Click on Sign Up button
            print("Step 1: Clicking on Sign Up button...")
            signup_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Button--link')]//span[text()='Sign Up']"))
            )
            signup_button.click()
            print("Step 1: Sign Up button clicked successfully.")

            # Step 2: Fill in the signup form
            print("Step 2: Filling in the signup form...")
            self._fill_form("username", self.test_data['username'])
            self._fill_form("email", self.test_data['email'])
            self._fill_form("password", self.test_data['password'])
            print("Step 2: Signup form filled successfully.")

            # Step 3: Submit form
            print("Step 3: Submitting the signup form...")
            submit_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.Button--primary[type='submit']"))
            )
            submit_button.click()
            print("Step 3: Signup form submitted successfully.")

            # Step 4: Verify success message
            print("Step 4: Verifying signup success message...")
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Welcome to Flarum')]"))
            )
            print("Test Result - Pass: User successfully registered.")
        except Exception as e:
            print(f"Test Result - Fail: An error occurred - {e}")
            self.driver.save_screenshot(f"signup_failure_{time.strftime('%Y%m%d-%H%M%S')}.png")
            print("Screenshot saved for debugging.")
            raise

    def _fill_form(self, field_name, value):
        """Helper method to fill form fields"""
        try:
            print(f"Filling in the '{field_name}' field...")
            field = self.wait.until(EC.element_to_be_clickable((By.NAME, field_name)))
            field.clear()
            field.send_keys(value)
            print(f"'{field_name}' field filled successfully.")
        except Exception as e:
            print(f"Error filling '{field_name}' field: {e}")
            raise

    @classmethod
    def tearDownClass(cls):
        """Clean up after the test suite"""
        print("Closing WebDriver...")
        if cls.driver:
            cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
