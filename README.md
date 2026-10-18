# Cookiecutter Data Science

A Cookie Cutter template for managing data science and machine learning projects, as we use it at <a href="https://acornanalytics.com">Acorn Analytics Inc</a>.

Project based on the <a href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>.

## Initial Project Structure


```
    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project
    ├── data
    │   ├── external       <- Data from third party sources
    │   ├── interim        <- Intermediate data that has been transformed
    │   ├── processed      <- The final, canonical data sets for modeling
    │   └── raw            <- The original, immutable data dump
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `2018-11-08-jqp-initial-data-exploration`
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials
    │
    ├── pyproject.toml     <- Project metadata and dependencies, managed with `uv`
    │
    └── src                <- Source code directory for the project
         ├─ __init__.py    <- Makes this src directory a Python module
         ├─ core.py        <- Refactored code goes here
         └─ utils.py       <- Helper functions that do not belong in `core.py`
```

## How to Use This Cookiecutter

- no install needed with `uv`. Create your project: on command line run `uvx cookiecutter https://github.com/acornanalytics/cookiecutter-data-science`
- Fill in the information as you are prompted
- `cd` into your new repo directory and check out the `README.md` file for further instructions and information


## Contributing

To contribute there are some things you need to do to get your environment set up.

- clone this repo
- run `uv sync` (the cookiecutter's own dependencies are listed in `requirements.txt`)


## TODOs

- Add notes about what is different than the original project by DrivenData
