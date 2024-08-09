.DEFAULT_GOAL := help

init:
    pip install -r requirements.txt

test:
    pytest tests

start:
    python main.py

clean:
    rm -rf __pycache__ *.pyc

# Yardım menüsünü gösterir
help:
    @echo "Commands:"
    @echo "  init     - installs dependencies"
    @echo "  test     - run tests"
    @echo "  start    - run project"
    @echo "  clean    - clean run for running with clear cache and memory"

.PHONY: init test start clean help
