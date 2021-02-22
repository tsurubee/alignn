name: JARVIS-DGL linting

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 4
      matrix:
        python-version: [3.7]

    steps:
    - uses: actions/checkout@v1
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v1
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
    - name: Lint with pycodestyle
      run: |
        pip install pycodestyle --upgrade
        pycodestyle --ignore E203,W503 --exclude=tests jarvisdgl
    - name: Lint with flake8
      run: |
        pip install flake8 --upgrade
        flake8 --ignore E203,W503 --exclude=tests --statistics --count --exit-zero jarvisdgl
    - name: Lint with pydoctstyle
      run: |
        pip install pydocstyle --upgrade
        pydocstyle --match-dir=core --match-dir=io --match-dir=io --match-dir=ai --match-dir=analysis --match-dir=db --match-dir=tasks --count jarvisdgl
