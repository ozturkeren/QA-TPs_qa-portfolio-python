import os
import sys
import pytest
import allure
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent  # tests/.. => project root
SRC_DIR = PROJECT_ROOT / "src"

for p in (str(PROJECT_ROOT), str(SRC_DIR)):
    if p not in sys.path:
        sys.path.insert(0, p)

@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com/"

@pytest.fixture(autouse=True)
def add_allure_environment():
    allure.dynamic.label("base_url", os.getenv("BASE_URL", "https://www.saucedemo.com/"))
