# FastAPI TDD Demo

## Overview

This repository contains the code for a demo on Test-Driven Development (TDD) with FastAPI. The goal of this project is to showcase how to implement TDD practices using FastAPI. 

> [!NOTE]
> It's a support for the presentation I made "Test Driven Development with FastAPI - Why you’re gonna use it after this talk"

## Directory Structure

The directory structure of this project is as follows:

```plaintext
fastapi_tdd/
├── 001_code_quality/
│   ├── __init__.py
│   ├── code_quality.py
│   └── test_code_quality.py
├── 002_bug_detection/
│   ├── __init__.py
│   ├── bug_detection.py
│   └── test_bug_detection.py
├── 003_easy_refactoring/
│   ├── __init__.py
│   ├── easy_refactoring.py
│   └── test_easy_refactoring.py
└── __init__.py
```

## Directory Descriptions

- **001_code_quality/**: Contains the code and tests for the first part of the demo, about how TDD improve your code quality.
  - **code_quality.py**: Contains the code for the first part of the slides.
  - **test_code_quality.py**: Contains the tests for the first part of the slides.
- **002_bug_detection/**: Contains the code and tests for the second part of the slides, about how TDD make it easier to find bugs.
  - **bug_detection.py**: Contains the code for the second part of the slides.
  - **test_bug_detection.py**: Contains the tests for the second part of the slides.
- **003_easy_refactoring/**: Contains the code and tests for the third part of the slides, about how TDD make it easier to refactor your code.
  - **easy_refactoring.py**: Contains the code for the third part of the slides.
  - **test_easy_refactoring.py**: Contains the tests for the third part of the slides.

## Features

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **TDD**: Demonstrates Test-Driven Development methodology.
- **Pytest**: A testing framework that makes it easy to write simple tests.

### Clone the Repository

```sh
git clone https://github.com/giuliowaitforitdavide/fastapi-tdd.git
cd fastapi-tdd
```

### Install the Dependencies

Make sure you have [Poetry](https://github.com/python-poetry/poetry) installed on your local machine. Then, run the following command to install the dependencies:

```sh
poetry install
```

### Run the Tests

You can run the tests using the following command:

```sh
pytest
```
