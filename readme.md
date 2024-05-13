# Invygo Mobile Test Automation Challenge
> Test automation challenge using Appium, Python and Pytest 


## Prerequisites
- Install and run Appium Server in the terminal
```
    npm i -g appium
    appium
```
- Install Java Development Kit (JDK) and set the environment variables
- Install Android Studio and create an Android Virtual Device (AVD) using AVD Manager
- Make sure the emulator is running before running the tests (check `adb devices` in the terminal)
- Make sure the python environment is set up

```
    python3 -m venv venv
    source venv/bin/activate
```


## Installation
Install python libraries

    ./venv/bin/pip3 install -r requirements.txt


Bash Runner
    
    bash runner.sh


CMD Runner

    ./venv/bin/python3 -m pytest src/spec/*.py --app=android; open ./report/pytest_html_report.html


## Test Report

- I have used my own html reporter `pytest-html-reporter` to generate the test report.
For reference:
    - https://github.com/prashanth-sams/pytest-html-reporter
    - https://pypi.org/project/pytest-html-reporter/
- Test report will be automatically generated inside `./report` directory after running the tests.
- I kept my existing test-runs in the `./report` directory for reference.
