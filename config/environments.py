import os
from dotenv import load_dotenv

load_dotenv()

class EnvironmentConfig:
    """Application and environment configuration."""
    BASE_URL = os.getenv("BASE_URL", "https://bugbash.online")
    RUN_ON_BSTACK = os.getenv("RUN_ON_BSTACK", "true").lower() in ("true", "1", "yes")
    DEFAULT_TIMEOUT_MS = int(os.getenv("DEFAULT_TIMEOUT_MS", "15000"))
    
    # Credentials for test personas
    USERS = {
        "demouser": {
            "username": "demouser",
            "password": "testingisfun99",
            "description": "Standard happy-path shopper"
        },
        "existing_orders_user": {
            "username": "existing_orders_user",
            "password": "testingisfun99",
            "description": "User with pre-existing orders history"
        },
        "fav_user": {
            "username": "fav_user",
            "password": "testingisfun99",
            "description": "User with pre-saved favorite items"
        },
        "image_not_loading_user": {
            "username": "image_not_loading_user",
            "password": "testingisfun99",
            "description": "Bug trigger: product images fail to load"
        },
        "locked_user": {
            "username": "locked_user",
            "password": "testingisfun99",
            "description": "Negative case: locked account validation"
        }
    }
