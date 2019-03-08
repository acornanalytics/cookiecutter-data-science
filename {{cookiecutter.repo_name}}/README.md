# {{cookiecutter.repo_name}}

{{cookiecutter.description}}

## Project Organization


```
    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project
    ├── data
    │   ├── external       <- Data from third party sources
    │   ├── interim        <- Intermediate data that has been transformed
    │   ├── processed      <- The final, canonical data sets for modeling
    │   └── raw            <- The original, immutable data dump
    │
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `{% now 'local', '%Y-%m-%d' %}-jqp-initial-data-exploration`
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    └── {{ cookiecutter.source_code_directory_name }}                <- Source code directory for the project
         ├─ __init__.py    <- Makes this src directory a Python module
         ├─ core.py        <- Refactored code goes here
         └─ utils.py       <- Where to store helper functions that do not belong in `core.py`
```

## Installation on Mac and Linux using `virtualenv`

- in the project directory `{{ cookiecutter.repo_name }}` run `virtualenv --python=/usr/local/bin/python3 venv`
- activate the environment with `source venv/bin/activate`
- edit the `.env` file and add `KEY=VALUE` for any items you wish to import (NOTE this will NOT be stored in Github. NEVER check this in to a repo!)

## Installation using `pipenv`

- make sure python3 and `pipenv` is installed on your system
- in the project directory `{{ cookiecutter.repo_name }}` run `virtualenv --python=/usr/local/bin/python3 venv`
- edit the `.env` file and add `KEY=VALUE` for any items you wish to import (NOTE this will NOT be stored in Github. NEVER check this in to a repo!)
- `cd` to the project directory and run `pipenv run python src/core.py` or whatever file you wish to run

### Running Jupyter Notebooks with `pipenv`

- `pipenv install ipykernel`
- `pipenv shell`
- `python -m ipykernel install --user`
- `jupyter notebook` will launch the notebook browser


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
