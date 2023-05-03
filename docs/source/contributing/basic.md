## Contributing to Pathfinder

The team takes welcomes contributions from other members of the organization.
In an effort to make that as straight-forward as possible we have documented our development approach in this group of documentation.
Please follow the guidelines outlined here and if you have any questions reach out for help.

### Dependency Management
Pathfinder uses Poetry combined with `pyproject.toml` to manage dependencies, set build configuration, and define useful tooling setups.
In order to contribute to Pathfinder you **must** first install [Poetry](https://python-poetry.org/)
Once Poetry is installed you should be able to manage dependencies easily with:

```
poetry install
```

### Code Style
Our code style is driven by the use of `black` and `flake8`.
In addition, we provide and [editorconfig](https://editorconfig.org) configuration to help configure your IDE

### Code Reviews
It is expected that before a code review is opened that all tests are passing,
that flake8 has not reported any issues, and that code has been formatted with black.

You can execute flake8 and black with the following commands:


