.PHONY: typing

typing:
	docker run --rm -v $(shell pwd)/homework/src:/src -w /src python:3.12-slim bash -c "pip install -r requirements.txt && mypy ."