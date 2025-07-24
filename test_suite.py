import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Actions.ActionPage import Action_Page, AddToCartPage, checkout


@pytest.fixture(scope="session")
def driver_setup():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")      # Run in headless mode
    #chrome_options.add_argument("--disable-gpu")   # Prevent GPU errors in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)                     # Wait implicitly up to 20s
    driver.maximize_window()                       # Maximize window (has no effect in headless, but harmless)
    yield driver

@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login_page = Action_Page(driver)
    login_page.login_url("https://www.saucedemo.com/")
    return login_page

def test_login_page_on_automation_customer_service_website(login):
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login_button()

def test_add_to_cart_page(login):
    add_to_cart = AddToCartPage(login.driver)
    add_to_cart.click_saucelabsbackpeak()
    add_to_cart.click_saucelabsbikelight()
    add_to_cart.click_saucelabsbolttshirt()
    add_to_cart.click_saucelabsfleecejacket()
    add_to_cart.click_saucelabsonesie()
    add_to_cart.click_testallthethingstshirtred()

def test_check_out_locator_page(login):
    check_out = checkout(login.driver)
    check_out.click_shoppingcartbadge()
    check_out.click_checkout()
    check_out.enter_firstname("Debbie")
    check_out.enter_lastname("Ego")
    check_out.enter_postalcode("postal_code")
    check_out.click_continue()
    check_out.click_finish()