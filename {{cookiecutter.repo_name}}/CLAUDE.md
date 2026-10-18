# CLAUDE.md

{{ cookiecutter.description }}

- Use `uv` for everything: `uv sync`, `uv run <command>`, `uv add <package>`. No `pip`, `virtualenv`, or `pipenv`.
- Code lives in `src/{{ cookiecutter.package_name }}/`; tests live in `tests/` and run with `uv run pytest`. Lint with `uv run ruff check`.
- Never commit the contents of `data/`, only the folder structure. `raw/` is immutable; write derived files to `interim/` and `processed/`.
- Never commit `.env` or credentials.
- Handoffs go in `handoffs/` (gitignored scratch state, never committed).
