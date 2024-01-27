<h1 align="center">
<img src="https://i.ibb.co/djVdtn9/ttp-logo.png" width="350">
</h1>

## 💪 Bringing the Power of tidyverse to Pandas!

**tidyversetopandas** is a Python package designed for users familiar with R's tidyverse who are transitioning to Python. It bridges the syntax gap between R and Python by offering pandas equivalents to popular tidyverse functions. This package is particularly beneficial for data scientists and analysts who seek to leverage pandas' robust capabilities with the familiar syntax of tidyverse.

- **Installation:** 🏗 WIP
- **Documentation:** 🏗 WIP
- **Source code:** https://github.com/UBC-MDS/TidyverseToPandas
- **Bug reports:** https://github.com/UBC-MDS/TidyverseToPandas/issues

### 🐍 Fitting into the Python Ecosystem

While pandas is a powerful tool for data manipulation in Python, it can be challenging for those accustomed to R's tidyverse syntax. `tidyversetopandas` is unique in its approach to blend these two worlds. In the Python ecosystem, `tidyversetopandas` fits alongside packages that aim to incorporate tidyverse-like functionality into Python's data manipulation landscape, predominantly with pandas. The goal is to make pandas more accessible to those accustomed to tidyverse syntax.Two notable packages in this domain are [tidypandas](https://github.com/tidypyverse/tidypandas) and [siuba](https://github.com/machow/siuba). Both of them represent, similar to `tidyversetopandas`, efforts to bridge the gap between R's tidyverse approach and Python's pandas library, offering users familiar with R's data manipulation tools a more comfortable transition to Python's data science ecosystem.

#### 🔑 Key Functions:

- `mutate():` Similar to its tidyverse counterpart, this function allows for the creation of new columns or modification of existing ones in a DataFrame.
- `filter():` Enables row-wise filtering, making it easier to sift through DataFrame based on specified conditions.
- `select():` Facilitates the selection of specific columns in a DataFrame, streamlining data manipulation and analysis.
- `arrange():` Offers sorting capabilities for DataFrame based on one or multiple columns.

## ⚙️ Installation

_Note: This package is currently under development and not yet available on PyPI. To install, please clone the repository and install the package locally. Follow the instructions in [Developer Guide](#Developer-Guide) to install the package in development mode._

```bash
$ pip install tidyversetopandas
```

## 🏃 Usage

Currently, the package is under development so follow [Developer Guide](#Developer-Guide) to install the package in development mode.

```python
from tidyversetopandas import tidyversetopandas

# Load your dataframe in pandas

# Use the functions:
df = ttp.mutate(df, b=lambda x: x["B"] * 2)
df = ttp.filter(df, "A > 1 and B < 6")
df = ttp.arrange(df, True, "A", "C")
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
