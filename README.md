# LoanPro Calculator CLI Test Suite

This repository contains an automated test suite for the LoanPro Calculator CLI application.

## Table of Contents

[Requirements](#requirements)

[Installation](#installation)

[Project Structure](#project-structure)

[Setting Tests](#setting-tests)

[Running the Tests](#running-the-tests)

[Contributing](#contributing)

[Reports](#reports)

[Findings](#findings)

## Requirements

- Python 3.6 or higher
- Docker

## Installation

1. Clone this repository:

    ```sh
    git clone https://github.com/TheAleRios/python-calculator-tests-challenge
    cd python-calculator-tests-challenge
    ```

2. Create a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```
## Project Structure
The project is organized as follows:
```bash
python-calculator-tests/
├── tests/                   # Directory containing the test file
│       └── calc_test.py     # Tests file
├── reports/                 # Folder to store generated reports
├── requirements.txt         # File to install required libraries
├── pytest.ini               # Pytest config file
└── README.md                # Read me file

```


## Automated Test Cases

The project includes 65 automated test cases, divided into the following categories:

### Loan Pro calculator tests
1. #### Common calculator tests

- Validation add calculations with real numbers.
- Validation subtract calculations with real numbers.
- Validation multiply calculations with real numbers.
- Validation divide calculations with real numbers.
- Validation add calculations with Infinity.
- Validation subtract calculations Infinity.
- Validation multiply calculations Infinity.
- Validation divide calculations Infinity.
- Validation for operations with real numbers with Inifinity results.


2. #### Error tests

- Validation of expected errors

## Setting Tests
The test are configurated in the pytest.ini file:


```bash
[pytest]
testpaths = tests
addotps = --html=reports/report.html --json-report --json-report-file=reports/report.json
```
This configuration set the test path to the folder "tests" and use html reports and json reports



## Running the Tests

1. To run the tests, go to root folder and run:

    ```sh
    pytest 
    ```
## Reports
Reports in html and json will be generated in the report folder after each test run. If already exists the existing reports will be updated. 

## Findings
All findings and bugs will go into Findings doc file in root folder.

## Contributing

If you want to contribute to this project, please open an issue or submit a pull request.