.PHONY: all run test

all: run

run:
	python3 -m puzzle

test:
	python3 -m pytest tests
