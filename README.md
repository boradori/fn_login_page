# Login Page Test

Libraries: selenium, pytest, pytest-env pytest-ordering, pytest-html

Install the libraries by running the following command:
```pip install -r requirements.txt```

Since we are using **pytest-env**, you need to make **pytest.ini** file in the root of the test suite.
```
touch pytest.ini
```
In **pytest.ini**, add the following snippet after replacing USERNAME and PASSWORD with your own. 
```
[pytest]
env =
    USERNAME=YOUR_VALID_USERNAME_COMES_HERE
    PASSWORD=YOUR_VALID_PASSWORD_COMES_HERE
    INVALID_USERNAME=ANY_INVALID_USERNAME_COMES_HERE
    INVALID_PASSWORD=ANY_INVALID_PASSWORD_COMES_HERE
```

## Execution:
```
py.test -v -s tests/login_test.py
```

Choose the browser of your choice. Default is Chrome. Choose from chrome, firefox, ie, and safari.
```
py.test -v -s tests/login_test.py --browser=firefox
```

If you need to generate test report in HTML, add --html=FILENAME.html

```
py.test -v -s tests/login_test.py --html=htmlreports.html
```

### Login test - invalid credential and successful login process
- **Valid login and logout**
- **Invalid login with wrong username and password**
- **Invalid login with blank password**
- **Invalid login with blank username**
- **Invalid login with blank username and password**
