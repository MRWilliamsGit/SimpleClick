install:
	pip install --upgrade pip &&\
		pip3 install -r requirements.txt

test:
	python3 -m pytest -vv test.py

format:
	black *.py

lint:
	pylint --disable=R,C clickmodel.py

all: install test format lint
