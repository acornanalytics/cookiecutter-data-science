from {{ cookiecutter.package_name }} import core


def test_main_runs():
    assert core.main() is None
