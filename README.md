# python-module-template

[![Lint Status](https://github.com/DNXLabs/python-module-template/workflows/Build/badge.svg)](https://github.com/DNXLabs/python-module-template/actions)
[![LICENSE](https://img.shields.io/github/license/DNXLabs/python-module-template)](https://github.com/DNXLabs/python-module-template/blob/master/LICENSE)


## Setup

#### Dependencies
- Python 3

#### Python Virtual Environment
```bash
# Create environment
python3 -m venv .venv

# To activate the environment
source .venv/bin/activate

# When you finish you can exit typing
deactivate
```

#### Install dev dependencies
```bash
#### Install dependencies and module
pip3 install -r requirements.txt
```

#### Install module
```bash
#### Install dependencies and module
pip3 install --editable .
```

#### --editable
It puts a link (actually *.pth files) into the python installation to your code, so that your package is installed, but any changes will immediately take effect.

This way all your test code, and client code, etc, can all import your package the usual way.

#### Run tests
```bash
python3 -m pytest
```

#### Build and Publish
Install and update dependencies:
```bash
python -m pip install --upgrade pip setuptools wheel twine
```

Build a binary wheel and a source tarball:
```bash
python setup.py sdist bdist_wheel
```

Publish distribution to PyPI:
```bash
python -m twine upload --repository testpypi dist/*
```

## Authors

Module managed by [DNX Solutions](https://github.com/DNXLabs).

## License

Apache 2 Licensed. See [LICENSE](https://github.com/DNXLabs/python-module-template/blob/master/LICENSE) for full details.