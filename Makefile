install:
	pip install --upgrade pip &&\
		pip3 install -r requirements.txt
	pip install torch==1.2.0+cpu torchvision==0.4.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

test:
	python3 -m pytest -vv test.py

format:
	black *.py

lint:
	pylint --disable=R,C main.py

all: install test format lint