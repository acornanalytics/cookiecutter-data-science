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
    ├── pyproject.toml     <- Project metadata and dependencies, managed with `uv`
    │
    ├── src/{{ cookiecutter.package_name }}   <- Source code for the project
    │    ├─ __init__.py    <- Makes this a Python module
    │    ├─ core.py        <- Refactored code goes here
    │    └─ utils.py       <- Helper functions that do not belong in `core.py`
    │
    └── tests              <- pytest tests
```

## Setup

This project uses [`uv`](https://docs.astral.sh/uv/) for everything: no `pip`, `virtualenv`, or `pipenv`.

- `uv sync` creates `.venv` and installs the dependencies from `pyproject.toml`
- `uv run python -m {{ cookiecutter.package_name }}.core` runs a script (or any other command: `uv run <command>`)
- `uv add <package>` adds a dependency
- `uv run pytest` runs the tests and `uv run ruff check` lints
- create a `.env` file and add `KEY=VALUE` for any secrets you need (it is gitignored, NEVER check it in to a repo)

### Running Jupyter Notebooks

- `uv run --with jupyter jupyter lab` launches the notebook browser without adding Jupyter to the project

## Data

The contents of `data/` are never committed, only the folder structure. Keep `raw/` immutable and write derived files to `interim/` and `processed/`.

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
