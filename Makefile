install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

brain-games:
	uv run brain-games