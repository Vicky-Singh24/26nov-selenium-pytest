# Python Interview Questions for QA Professionals

## Basic Python Questions

### 1. What are the different data types in Python?
**Answer:** Python has several built-in data types:
- **Numeric:** int, float, complex
- **Sequence:** list, tuple, range, string
- **Boolean:** bool
- **Set:** set, frozenset
- **Dictionary:** dict
- **None:** NoneType

### 2. What is the difference between list and tuple in Python?
**Answer:**
- **List:** Mutable (can be modified), uses square brackets `[]`, slower
- **Tuple:** Immutable (cannot be modified), uses parentheses `()`, faster
- Example: 
  ```python
  my_list = [1, 2, 3]  # Can be modified
  my_tuple = (1, 2, 3)  # Cannot be modified
  ```

### 3. What are Python decorators?
**Answer:** Decorators are functions that modify the behavior of other functions or methods. They are commonly used in testing frameworks.
```python
@pytest.fixture
def setup():
    print("Setup")
```

### 4. Explain the difference between `==` and `is` in Python.
**Answer:**
- `==` compares the values of two objects
- `is` compares the identity (memory address) of two objects
```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b  # True (same values)
a is b  # False (different objects)
```

### 5. What is list comprehension?
**Answer:** A concise way to create lists based on existing lists or iterables.
```python
# Traditional approach
squares = []
for i in range(10):
    squares.append(i**2)

# List comprehension
squares = [i**2 for i in range(10)]
```

## Object-Oriented Programming

### 6. What are the four pillars of OOP?
**Answer:**
1. **Encapsulation:** Bundling data and methods that work on that data
2. **Inheritance:** Creating new classes from existing classes
3. **Polymorphism:** Using a single interface for different data types
4. **Abstraction:** Hiding complex implementation details

### 7. What is the difference between `__init__` and `__new__` methods?
**Answer:**
- `__new__` is called before object creation (allocates memory)
- `__init__` is called after object creation (initializes the object)

### 8. What is method overriding in Python?
**Answer:** When a child class provides a specific implementation of a method already defined in the parent class.
```python
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")
```

## Testing Framework Questions

### 9. What is pytest and how is it different from unittest?
**Answer:**
- **pytest:** More Pythonic, supports fixtures, parametrization, and has simpler syntax
- **unittest:** Built-in Python module, follows xUnit style, requires more boilerplate
- pytest can run unittest tests but not vice versa

### 10. What are pytest fixtures?
**Answer:** Fixtures are functions that provide data or setup/teardown operations for tests. They promote code reusability.
```python
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
```

### 11. What is parametrization in pytest?
**Answer:** Running the same test with different input values.
```python
@pytest.mark.parametrize("username,password", [
    ("admin", "admin123"),
    ("user1", "pass123"),
    ("user2", "pass456")
])
def test_login(username, password):
    # Test login with different credentials
    pass
```

### 12. What are pytest markers?
**Answer:** Markers are used to categorize tests and run specific groups of tests.
```python
@pytest.mark.smoke
def test_critical_feature():
    pass

@pytest.mark.regression
def test_existing_feature():
    pass

# Run: pytest -m smoke
```

### 13. What is the purpose of conftest.py?
**Answer:** conftest.py is used to define fixtures and hooks that are shared across multiple test files in a directory or package.

## Selenium with Python Questions

### 14. What are the different types of waits in Selenium?
**Answer:**
1. **Implicit Wait:** Waits for a specified time before throwing NoSuchElementException
   ```python
   driver.implicitly_wait(10)
   ```
2. **Explicit Wait:** Waits for a specific condition to be met
   ```python
   wait = WebDriverWait(driver, 10)
   element = wait.until(EC.presence_of_element_located((By.ID, "myId")))
   ```
3. **Fluent Wait:** Similar to explicit wait with polling interval and ignore exceptions

### 15. What are the different locator strategies in Selenium?
**Answer:**
- ID: `By.ID`
- Name: `By.NAME`
- Class Name: `By.CLASS_NAME`
- Tag Name: `By.TAG_NAME`
- Link Text: `By.LINK_TEXT`
- Partial Link Text: `By.PARTIAL_LINK_TEXT`
- XPath: `By.XPATH`
- CSS Selector: `By.CSS_SELECTOR`

### 16. How do you handle alerts in Selenium?
**Answer:**
```python
alert = driver.switch_to.alert
alert.accept()  # Click OK
alert.dismiss()  # Click Cancel
alert.send_keys("text")  # Enter text in prompt
text = alert.text  # Get alert text
```

### 17. How do you handle dropdowns in Selenium?
**Answer:**
```python
from selenium.webdriver.support.ui import Select

dropdown = Select(driver.find_element(By.ID, "dropdown"))
dropdown.select_by_visible_text("Option 1")
dropdown.select_by_value("value1")
dropdown.select_by_index(0)
```

### 18. What is Page Object Model (POM)?
**Answer:** A design pattern where web pages are represented as classes, and page elements as variables. Actions on pages are implemented as methods. This improves code reusability and maintainability.
```python
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login")
    
    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
```

## Advanced Python Questions

### 19. What is the difference between deep copy and shallow copy?
**Answer:**
- **Shallow copy:** Creates a new object but references the same nested objects
- **Deep copy:** Creates a new object and recursively copies all nested objects
```python
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)
```

### 20. What are lambda functions?
**Answer:** Anonymous functions defined with the `lambda` keyword.
```python
# Regular function
def square(x):
    return x ** 2

# Lambda function
square = lambda x: x ** 2
```

### 21. What is the difference between @staticmethod and @classmethod?
**Answer:**
- **@staticmethod:** Doesn't receive implicit first argument (no self or cls)
- **@classmethod:** Receives the class as implicit first argument (cls)
```python
class MyClass:
    @staticmethod
    def static_method():
        return "Static"
    
    @classmethod
    def class_method(cls):
        return f"Class: {cls.__name__}"
```

### 22. What are generators in Python?
**Answer:** Functions that use `yield` to return values lazily, one at a time, saving memory.
```python
def number_generator(n):
    for i in range(n):
        yield i

gen = number_generator(5)
for num in gen:
    print(num)
```

### 23. What is the purpose of `*args` and `**kwargs`?
**Answer:**
- `*args`: Passes variable number of positional arguments
- `**kwargs`: Passes variable number of keyword arguments
```python
def my_function(*args, **kwargs):
    print(args)    # Tuple of positional arguments
    print(kwargs)  # Dictionary of keyword arguments

my_function(1, 2, 3, name="John", age=30)
```

## Exception Handling

### 24. How do you handle exceptions in Python?
**Answer:**
```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No exception occurred")
finally:
    print("Always executed")
```

### 25. What is the difference between `raise` and `assert`?
**Answer:**
- `raise`: Explicitly raises an exception
- `assert`: Raises AssertionError if condition is False (used for debugging)
```python
# raise
if age < 0:
    raise ValueError("Age cannot be negative")

# assert
assert age >= 0, "Age cannot be negative"
```

## File Handling and Data Management

### 26. How do you read and write files in Python?
**Answer:**
```python
# Reading
with open('file.txt', 'r') as f:
    content = f.read()

# Writing
with open('file.txt', 'w') as f:
    f.write("Hello World")

# Appending
with open('file.txt', 'a') as f:
    f.write("New line")
```

### 27. How do you work with JSON data in Python?
**Answer:**
```python
import json

# Convert Python dict to JSON string
data = {"name": "John", "age": 30}
json_string = json.dumps(data)

# Convert JSON string to Python dict
python_dict = json.loads(json_string)

# Read from JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

# Write to JSON file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
```

### 28. How do you work with CSV files?
**Answer:**
```python
import csv

# Reading CSV
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Writing CSV
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['John', '30'])
```

## API Testing Questions

### 29. How do you make HTTP requests in Python for API testing?
**Answer:**
```python
import requests

# GET request
response = requests.get('https://api.example.com/users')
print(response.status_code)
print(response.json())

# POST request
data = {"username": "test", "password": "test123"}
response = requests.post('https://api.example.com/login', json=data)

# Headers
headers = {"Authorization": "Bearer token123"}
response = requests.get('https://api.example.com/profile', headers=headers)
```

### 30. How do you validate API responses in pytest?
**Answer:**
```python
import pytest
import requests

def test_api_status_code():
    response = requests.get('https://api.example.com/users')
    assert response.status_code == 200

def test_api_response_data():
    response = requests.get('https://api.example.com/user/1')
    data = response.json()
    assert data['id'] == 1
    assert 'name' in data
    assert isinstance(data['name'], str)
```

## Database Questions

### 31. How do you connect to a database in Python?
**Answer:**
```python
import sqlite3

# SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM users')
results = cursor.fetchall()
conn.close()

# MySQL
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="testdb"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()
conn.close()
```

## Test Automation Best Practices

### 32. What are some best practices for test automation?
**Answer:**
1. Follow the DRY (Don't Repeat Yourself) principle
2. Use Page Object Model for UI tests
3. Write independent and isolated tests
4. Use meaningful test names
5. Implement proper wait strategies
6. Use data-driven testing
7. Maintain test data separately
8. Implement proper logging and reporting
9. Use version control for test scripts
10. Keep tests maintainable and readable

### 33. How do you implement data-driven testing in pytest?
**Answer:**
```python
import pytest

# Using parametrize
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 54),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

# Reading from external file
import csv

def get_test_data():
    with open('testdata.csv', 'r') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

@pytest.mark.parametrize("data", get_test_data())
def test_with_csv_data(data):
    assert data['expected'] == data['actual']
```

### 34. How do you generate test reports in pytest?
**Answer:**
```python
# Install pytest-html
# pip install pytest-html

# Run tests with HTML report
# pytest --html=report.html --self-contained-html

# Install allure-pytest
# pip install allure-pytest

# Generate allure report
# pytest --alluredir=./allure-results
# allure serve ./allure-results
```

### 35. What is continuous integration and how does it relate to test automation?
**Answer:** CI is a practice where code changes are automatically built, tested, and integrated into the shared repository frequently. Test automation scripts are executed as part of CI pipeline to provide quick feedback on code quality.

Example CI tools: Jenkins, GitLab CI, GitHub Actions, CircleCI

## Scenario-Based Questions

### 36. How would you handle a flaky test?
**Answer:**
1. Identify the root cause (timing issues, dynamic data, environmental dependencies)
2. Implement proper wait strategies (explicit waits)
3. Make test data independent
4. Add retry mechanisms for genuine intermittent issues
5. Isolate tests properly
6. Use pytest-rerunfailures plugin if needed

### 37. How do you handle dynamic web elements in Selenium?
**Answer:**
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Wait for element to be present
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "dynamic-id")))

# Wait for element to be clickable
element = wait.until(EC.element_to_be_clickable((By.ID, "button")))

# Wait for element to be visible
element = wait.until(EC.visibility_of_element_located((By.ID, "modal")))
```

### 38. How would you test a login functionality?
**Answer:**
```python
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin:
    
    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com/login")
        yield
        self.driver.quit()
    
    def test_valid_login(self, setup):
        self.driver.find_element(By.ID, "username").send_keys("valid_user")
        self.driver.find_element(By.ID, "password").send_keys("valid_pass")
        self.driver.find_element(By.ID, "login").click()
        assert "Dashboard" in self.driver.title
    
    def test_invalid_login(self, setup):
        self.driver.find_element(By.ID, "username").send_keys("invalid_user")
        self.driver.find_element(By.ID, "password").send_keys("invalid_pass")
        self.driver.find_element(By.ID, "login").click()
        error_msg = self.driver.find_element(By.CLASS_NAME, "error").text
        assert "Invalid credentials" in error_msg
    
    def test_empty_credentials(self, setup):
        self.driver.find_element(By.ID, "login").click()
        assert "Please enter username" in self.driver.page_source
```

### 39. How do you handle multiple windows/tabs in Selenium?
**Answer:**
```python
# Get current window handle
main_window = driver.current_window_handle

# Click element that opens new window
driver.find_element(By.ID, "new-window-link").click()

# Get all window handles
all_windows = driver.window_handles

# Switch to new window
for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)
        # Perform actions in new window
        break

# Switch back to main window
driver.switch_to.window(main_window)
```

### 40. How do you take screenshots on test failure?
**Answer:**
```python
import pytest
from selenium import webdriver
from datetime import datetime

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            screenshot_name = f"screenshot_{item.name}_{timestamp}.png"
            driver.save_screenshot(screenshot_name)
```

## Tips for Interview Success

1. **Understand the fundamentals:** Have a strong grasp of Python basics
2. **Know your testing framework:** Be comfortable with pytest or unittest
3. **Practice Selenium:** Work on real-world automation scenarios
4. **Code readability:** Write clean, maintainable code
5. **Problem-solving:** Think through problems step by step
6. **Ask questions:** Clarify requirements before implementing solutions
7. **Stay updated:** Keep learning new tools and best practices
8. **Real-world experience:** Share examples from your actual projects

---

**Note:** These questions cover the essential topics for QA professionals working with Python. Practice implementing these concepts in real automation projects to build confidence.
