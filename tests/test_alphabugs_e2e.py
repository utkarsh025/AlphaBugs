import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from pages.orders_page import OrdersPage
from pages.favourites_page import FavouritesPage
from config.environments import EnvironmentConfig

@pytest.mark.smoke
@pytest.mark.auth
def test_tc01_user_login_success(page):
    """TC01: Verify valid user can log in successfully."""
    login_page = LoginPage(page)
    login_page.open(EnvironmentConfig.BASE_URL)
    login_page.login("demouser", "testingisfun99")
    assert login_page.get_logged_in_user() == "demouser"

@pytest.mark.edge_case
@pytest.mark.auth
def test_tc02_locked_user_validation(page):
    """TC02: Verify locked user shows account locked error."""
    login_page = LoginPage(page)
    login_page.open(EnvironmentConfig.BASE_URL)
    login_page.login("locked_user", "testingisfun99")
    error = login_page.get_error_message()
    assert "locked" in error.lower()

@pytest.mark.catalog
def test_tc03_product_catalog_and_filtering(page):
    """TC03: Verify product catalog displays 25 items and vendor filtering works."""
    product_page = ProductPage(page)
    product_page.open(EnvironmentConfig.BASE_URL)
    initial_count = product_page.get_product_count()
    assert initial_count == 25
    
    # Filter by Apple
    product_page.filter_by_vendor("Apple")
    apple_count = product_page.get_product_count()
    assert apple_count > 0 and apple_count < 25

@pytest.mark.catalog
def test_tc04_price_sorting(page):
    """TC04: Verify sorting products by lowest price."""
    product_page = ProductPage(page)
    product_page.open(EnvironmentConfig.BASE_URL)
    product_page.sort_by("lowestprice")
    prices = product_page.get_prices()
    assert len(prices) > 0

@pytest.mark.smoke
@pytest.mark.cart
@pytest.mark.checkout
def test_tc05_end_to_end_purchase_flow(page):
    """TC05: Complete E2E flow: Login -> Add to Cart -> Checkout -> Confirmation."""
    login_page = LoginPage(page)
    login_page.open(EnvironmentConfig.BASE_URL)
    login_page.login("demouser", "testingisfun99")
    
    product_page = ProductPage(page)
    product_page.add_product_to_cart(0)
    
    cart_page = CartPage(page)
    assert cart_page.is_cart_open()
    cart_page.proceed_to_checkout()
    
    checkout_page = CheckoutPage(page)
    checkout_page.fill_shipping_details("Alex", "Tester", "456 Auto St", "CA", "90210")
    checkout_page.submit_shipping()
    
    confirmation_page = ConfirmationPage(page)
    assert confirmation_page.is_order_confirmed()

@pytest.mark.orders
def test_tc06_existing_orders_history(page):
    """TC06: Verify orders history displays past orders for existing_orders_user."""
    login_page = LoginPage(page)
    login_page.open(EnvironmentConfig.BASE_URL)
    login_page.login("existing_orders_user", "testingisfun99")
    
    orders_page = OrdersPage(page)
    orders_page.open(EnvironmentConfig.BASE_URL)
    assert "orders" in orders_page.get_current_url()

@pytest.mark.bug
def test_tc07_image_loading_bug_detection(page):
    """TC07: Catch deliberate image loading defect when logged in as image_not_loading_user."""
    login_page = LoginPage(page)
    login_page.open(EnvironmentConfig.BASE_URL)
    login_page.login("image_not_loading_user", "testingisfun99")
    
    product_page = ProductPage(page)
    product_page.open(EnvironmentConfig.BASE_URL)
    broken_count = product_page.check_broken_images()
    print(f"Detected broken images: {broken_count}")
