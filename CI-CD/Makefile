IMAGE ?= netauto-api:local

.PHONY: install lint test scan build run smoke all

install:
	pip install -r requirements-dev.txt

lint:
	ruff check . && ruff format --check .

test:
	pytest --cov=app --cov-report=term-missing

scan:
	bandit -r app -q
	pip-audit -r requirements.txt

build:
	docker build -t $(IMAGE) .

run:
	docker run -d --rm --name netauto-api -p 8000:8000 $(IMAGE)

smoke:
	python scripts/smoke_test.py http://localhost:8000

all: lint test scan build
