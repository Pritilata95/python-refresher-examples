# Calculator

A simple Python package for basic arithmetic operations.

## Installation

To install the `calculator` package, use the following command:

```bash
pip install -e .
```

To uninstall the package, use the following command:

```bash
pip uninstall calculator -y
```

## Usage
You can use the calculator package to perform basic arithmetic operations such as addition,
subtraction, multiplication, and division.
```
from calculator import add, subtract, multiply, divide

print(add(10, 5))          # Output: 15
print(subtract(10, 5))     # Output: 5
print(multiply(10, 5))     # Output: 50
print(divide(10, 5))       # Output: 2.0
```

## Project Structure
This project has the following structure:

```
example-python-package/
├── calculator/
│   ├── __init__.py
│   ├── arithmetic.py
├── tests/
│   ├── __init__.py
│   ├── test_arithmetic.py
├── .gitignore
├── LICENSE
├── main.py
├── pyproject.toml
└── README.md
```

## Running Tests
To run the tests, use the following command:
```
python -m unittest discover -s tests
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.