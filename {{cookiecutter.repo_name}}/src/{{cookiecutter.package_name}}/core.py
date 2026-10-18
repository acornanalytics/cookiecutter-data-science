"""Core logic for {{ cookiecutter.project_name }}."""

import logging

log = logging.getLogger(__name__)


def main() -> None:
    """Run the project's main process."""
    log.info("TODO: run the project's main process")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%b %d %H:%M:%S")
    main()
