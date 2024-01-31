# TEST RELEASE AGAIN AGAIN AGAIN AGAIN
<h1 align="center">
<img src="https://i.ibb.co/djVdtn9/ttp-logo.png" width="350">
</h1>

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![Python 3.9.0](https://img.shields.io/badge/python-3.9.0-blue.svg)](https://www.python.org/downloads/release/python-390/) [![codecov](https://codecov.io/gh/UBC-MDS/TidyverseToPandas/branch/main/graph/badge.svg?token=3Z3Z3Z3Z3Z)](https://codecov.io/gh/UBC-MDS/TidyverseToPandas) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![version](https://img.shields.io/pypi/v/tidyversetopandas)](https://pypi.org/project/tidyversetopandas/)[![Documentation Status](https://readthedocs.org/projects/tidyversetopandas/badge/?version=latest)](https://tidyversetopandas.readthedocs.io/en/latest/?badge=latest) [![PyPI version](https://badge.fury.io/py/tidyversetopandas.svg)](https://badge.fury.io/py/tidyversetopandas)

## 💪 Bringing the Power of tidyverse to Pandas!

**tidyversetopandas** is a Python package designed for users familiar with R's tidyverse who are transitioning to Python. It bridges the syntax gap between R and Python by offering pandas equivalents to popular tidyverse functions. This package is particularly beneficial for data scientists and analysts who seek to leverage pandas' robust capabilities with the familiar syntax of tidyverse.

- **Installation:** [installation](#%EF%B8%8F-installation)
- **Documentation:** [https://tidyversetopandas.readthedocs.io/en/latest/example.html](https://tidyversetopandas.readthedocs.io/en/latest/example.html)
- **Source code:** [https://github.com/UBC-MDS/TidyverseToPandas](https://github.com/UBC-MDS/TidyverseToPandas)
- **Bug reports:** [https://github.com/UBC-MDS/TidyverseToPandas/issues](https://github.com/UBC-MDS/TidyverseToPandas/issues)

### 🐍 Fitting into the Python Ecosystem

While pandas is a powerful tool for data manipulation in Python, it can be challenging for those accustomed to R's tidyverse syntax. `tidyversetopandas` is unique in its approach to blend these two worlds. In the Python ecosystem, `tidyversetopandas` fits alongside packages that aim to incorporate tidyverse-like functionality into Python's data manipulation landscape, predominantly with pandas. The goal is to make pandas more accessible to those accustomed to tidyverse syntax.Two notable packages in this domain are [tidypandas](https://github.com/tidypyverse/tidypandas) and [siuba](https://github.com/machow/siuba). Both of them represent, similar to `tidyversetopandas`, efforts to bridge the gap between R's tidyverse approach and Python's pandas library, offering users familiar with R's data manipulation tools a more comfortable transition to Python's data science ecosystem.

#### 🔑 Key Functions:

- `mutate():` Similar to its tidyverse counterpart, this function allows for the creation of new columns or modification of existing ones in a DataFrame.
- `filter():` Enables row-wise filtering, making it easier to sift through DataFrame based on specified conditions.
- `select():` Facilitates the selection of specific columns in a DataFrame, streamlining data manipulation and analysis.
- `arrange():` Offers sorting capabilities for DataFrame based on one or multiple columns.

## ⚙️ Installation

```bash
pip install tidyversetopandas
```

## 🏃 Usage

Lets try to use `tidyversetopandas`.

### Import package

Import the package into your Python environment after installation:

```python
from tidyversetopandas import tidyversetopandas as ttp
```

### Loading Data

Begin by loading your data into a pandas dataframe. This package assumes that you have a dataframe ready for manipulation named `df`.

### Mutate

Use `mutate` to create new columns or modify existing ones. We can do this by writing the expression we want as a string.

```
df = ttp.mutate(df, "b=b*2")
```

### Filter

The `filter` function is used to subset dataframes based on specified conditions. For instance, to select rows where 'A' is greater than 1 and 'B' is less than 6

```
df = ttp.filter(df, "A > 1 and B < 6")
```

### Arrange

Sort your dataframe with `arrange`. You can sort by multiple columns and specify ascending or descending order. For example, to sort by 'A' in ascending order and then by 'C'

```
df = ttp.arrange(df, True, "A", "C")
```

### Select

To keep only certain columns, use the `select` function. For example, to keep only the column 'A'

```
df = ttp.select(df, "A")
```

## 📖 Developer Guide

### 🛠️ Installation in Development Mode

1. Clone the repository and navigate to the project root directory.

2. Create a virtual environment and activate it.

```bash
conda env create -f environment.yml
conda activate tidyversetopandas
```

3. Make sure `poetry` is installed. If not, install it [here](https://python-poetry.org/docs/). Once installed, run the following command to install the package in development mode.

```bash
poetry install
```

### ✅ Testing

To run the tests, use the following command:

```bash
pytest tests/
```

To run tests with coverage, use the following command:

```bash
pytest tests/ --cov=tidyversetopandas
```

To view the coverage report, use the following command:

```bash
pytest --cov=tidyversetopandas --cov-report html tests/
```
This will create a `htmlcov` directory containing the coverage report in HTML format. Open the index.html file in this directory with a web browser to view the detailed coverage report.

## 🤝 Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## ©️ License

`tidyversetopandas` was created by Thomas,Sophia,Lily,Nando. It is licensed under the terms of the MIT license.

## 👥 Contributors

1. [Thomas Jian](https://github.com/786213750)
2. [Sophia Zhao](https://github.com/zth96)
3. [Lily Tao](https://github.com/LilyTao0531)
4. [Farrandi Hernando](https://github.com/farrandi)

## Credits

`tidyversetopandas` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
