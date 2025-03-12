install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

gendiff:
	uv run gendiff

lint:
	uv run ruff check gendiff
