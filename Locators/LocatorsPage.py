from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

class AddToCartLocators:
    SAUCELABSBACKPEAK = (By.ID, "add-to-cart-sauce-labs-backpack")
    SAUCELABSBIKELIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    SAUCELABSBOLTTSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    SAUCELABSFLEECEJACKET = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    SAUCELABSONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    TESTALLTHETHINGSTSHIRTRED = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")

class CheckoutLocator:
    SHOPPINGCARTBADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CHECKOUT = (By.ID, "checkout")
    FIRSTNAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    POSTALCODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")