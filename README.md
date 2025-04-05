# Portfolio web Python Playwright project

This is a portfolio project created to automate the functionality of the [Google Translate](https://translate.google.com/) website using Python and Playwright framework. The primary goal is to showcase my test automation skills through functional tests that check the language selection features on Google Translate.

> [!NOTE]
> The project was created to demonstrate my test automation skills, there was no goal to cover all functionality and views of Google Translate

## Table of Contents
- [Features](#features)
- [Structure](#structure)
- [Setup Project and Run Tests Locally](#setup-project-and-run-tests-locally)
- [Built With](#built-with)
- [License](#license)

## Features 
- Automating interactions on the Google Translate website
- Using Python and pytest for test automation
- Running autotests on Chrome and Firefox browsers

## Structure
- `google-translate-autotests/`: Folder containing test cases for functional tests.
- `pages/`: Folder with page object models to interact with Google Translate UI.
- `data/`: Data files for test configuration and input values.

## Setup Project and Run Tests Locally

### 1. Precondition
- Python 3.7 or higher installed
- pytest and selenium libraries installed

### 2. Setup Project
- Clone the repository:

    ```bash
    git clone https://github.com/portfolio-web-python-playwright-project.git
    cd portfolio-web-python-playwright-project
    ```

- Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

##№ 3. Run Tests:
To run **all tests** locally using pytest:

```bash
pytest --maxfail=1 --disable-warnings -q
```
## Built With
- [Python](https://www.python.org/) - The programming language used for writing the automation scripts
- [PyTest](https://pytest.org/) - The testing framework used to run the tests

## License
```
MIT License

Copyright (c) 2025 Yevhenii Marchenko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```