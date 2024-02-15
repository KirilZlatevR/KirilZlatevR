from selenium.webdriver.common.by import By
import BasePage.BasePage as basePage

userSignInButton = basePage.driver.find_element(By.XPATH, "//button[@data-testid = 'user-sign-in']")
