.PHONY: clean python-packages install run all

# =============================================================================
# PYTHON
# =============================================================================

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name __pycache__ -delete

python-packages:
	pip install -r requirements.txt

install: python-packages

run:
	python code/main.py

all: clean install run
