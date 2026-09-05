# AlphaBugs - BrowserStack Testathon 2026

![BrowserStack](https://img.shields.io/badge/BrowserStack-Automate%20%7C%20Observability%20%7C%20Test%20Management-orange?style=for-the-badge&logo=browserstack)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python)
![Playwright](https://img.shields.io/badge/Playwright-E2E%20Testing-green?style=for-the-badge&logo=playwright)
![CI/CD](https://img.shields.io/badge/GitHub%20Actions-Automated%20CI-purple?style=for-the-badge&logo=githubactions)

## 📌 Project Overview
**AlphaBugs** is an end-to-end test automation suite built for the BrowserStack Testathon. It implements a scalable **Page Object Model (POM)** architecture using **Python + Playwright** and connects to BrowserStack Cloud to execute cross-browser and cross-platform tests across Desktop and Mobile devices.

The target application under test is [https://bugbash.online/?signin=true](https://bugbash.online/?signin=true).

---

## 🏆 Testathon Submission Deliverables

| Deliverable | Description | Link |
|---|---|---|
| **Step 1: Test Management** | Documented test suite with critical user flows and edge cases | *https://test-management.browserstack.com/projects/4097466/folder/56644980/test-cases?public_token=c4c8460fcd8f9a02356df89da58c2ccecf2cce602e23fa082f46672b8666dc4b28b48a3f09b429a77f44cf3400003c63ab3834f686bcfa9485e6636a5d9db3a7&public_token_id=24088* |
| **Step 2: Functional Automation Suite** | Complete source code with BrowserStack integration | [GitHub Repository](https://github.com/utkarsh025/AlphaBugs) |
| **Step 3: Test Runs in Test Management** | Test run results linked with Test Management | *https://test-management.browserstack.com/projects/4097466/builds/AlphaBugs+Testathon+Full+Suite/1?public_token=a7ae96973d8874c2e2deb7c33693fc1a960f2d31a3615280096696fa1605ca18f186b55d6f18fc65c41e0894a1e67a3b6a01435beefa7c4d3c72e221b1425909&public_token_id=24087* |

---

## 🏗️ Architecture & Project Structure

```
AlphaBugs/
├── .github/
│   └── workflows/
│       └── browserstack.yml     # GitHub Actions CI/CD Pipeline
├── config/
│   ├── browserstack_config.py   # CDP URL builder & platform capabilities
│   └── environments.py          # Personas, URLs, timeouts
├── pages/
│   ├── base_page.py             # Reusable Playwright actions & BStack telemetry
│   ├── login_page.py            # Authentication & session controls
│   ├── product_page.py          # Catalog, vendor filters, sorting
│   ├── cart_page.py             # Floating cart drawer interactions
│   ├── checkout_page.py         # Shipping form inputs & submit
│   ├── confirmation_page.py     # Order receipt verification
│   ├── orders_page.py           # Past order history inspection
│   └── favourites_page.py       # Wishlist validation
├── tests/
│   ├── conftest.py              # Pytest fixture (BStack CDP / Local execution)
│   └── test_alphabugs_e2e.py    # Test suite covering TC01 - TC07
├── test_data/
│   └── test_data.json           # Data fixtures & personas
├── utils/
│   ├── bstack_helper.py         # Step annotations, status reporting & API
│   └── logger.py                # Standardized execution logging
├── .env.example                 # Safe credential template
├── .gitignore                   # Ignored files (secrets, caches)
├── browserstack.yml             # BrowserStack SDK platform matrix
├── pytest.ini                   # Test configuration and markers
└── requirements.txt             # Python dependencies
```

---

## 🎯 Test Scenarios Covered

1. **TC01 - Authentication**: Valid user login (`demouser`) and state persistence.
2. **TC02 - Negative Validation**: Account lock validation for `locked_user` ("Your account has been locked.").
3. **TC03 - Product Catalog & Filtering**: Initial product inventory count (25 items) and brand filtering (Apple, Samsung, Google, OnePlus).
4. **TC04 - Price Sorting**: Numeric sorting validation by price (Lowest to Highest).
5. **TC05 - End-to-End Purchase Flow**: Complete critical journey: Login -> Add to Cart -> Checkout -> Shipping Details -> Order Confirmation receipt.
6. **TC06 - Order History**: Inspection of existing order history for `existing_orders_user`.
7. **TC07 - Bug Detection**: Identification of broken product images when logged in as `image_not_loading_user`.

---

## 🐛 Bug Detection Report

| Bug ID | Persona / Trigger | Observed Behavior | Expected Behavior |
|---|---|---|---|
| **BUG-01** | `image_not_loading_user` | Product thumbnails fail to load (broken image links). | All product images should load valid asset URLs. |
| **BUG-02** | Cart install calculation | Inconsistent rounding on monthly installment calculations for multi-item cart. | Accurate arithmetic sum matching product installments. |
| **BUG-03** | Sorting logic | String vs numeric sort discrepancies when comparing 3-digit and 4-digit prices. | Numeric price comparison order. |

---

## 🚀 How to Run

### 1. Setup Environment
```bash
git clone https://github.com/utkarsh025/AlphaBugs.git
cd AlphaBugs
python -m venv .venv
source .venv/bin/activate  # Or on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Credentials
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Fill in your credentials:
```ini
BROWSERSTACK_USERNAME=your_username
BROWSERSTACK_ACCESS_KEY=your_access_key
RUN_ON_BSTACK=true
```

### 3. Run Tests on BrowserStack Cloud
```bash
pytest tests/ -v
```

### 4. Run Smoke Tests Only
```bash
pytest -m smoke
```
