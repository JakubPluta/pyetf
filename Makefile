ifeq ($(OS),Windows_NT)
    os := Windows
else
    os := $(shell uname)
endif

pretty:
	isort etfpy/ && isort tests/
	black etfpy/ && black tests/

test:
	pytest tests/ -vv -ss
cov:
	coverage run --source=etfpy -m pytest tests/ -vv -ss && coverage report -m
scrape:
	python etfpy/scripts/scrape_etfs.py
