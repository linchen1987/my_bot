.PHONY: help install dev-install test run lint clean sync-deps

help:
	@echo "Available commands:"
	@echo "  make install       - Install main dependencies"
	@echo "  make dev-install   - Install main and dev dependencies (includes pytest)"
	@echo "  make test          - Run tests with pytest"
	@echo "  make test-cov      - Run tests with coverage"
	@echo "  make lint          - Run linter"
	@echo "  make run           - Run the main script"
	@echo "  make sync-deps     - Sync dependencies with uv"
	@echo "  make clean         - Clean venv and cache"

install:
	uv venv --seed
	uv pip install .

dev-install:
	uv venv --seed
	uv sync --extra dev

test:
	uv run pytest -v

test-cov:
	uv run pytest -v --cov=. --cov-report=html

lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff format .

run:
	uv run python main.py

sync-deps:
	uv sync

clean:
	rm -rf .venv
	rm -rf .ruff_cache
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
