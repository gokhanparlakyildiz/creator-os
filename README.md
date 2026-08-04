# Creator OS

Creator OS is a modular AI operating system for autonomous digital creators.

The project will bring trend discovery, creator memory, prompt compilation, and
content workflows together behind small, testable Python modules.

## Status

Creator OS is in its foundation phase. The current repository establishes the
Python package, quality tooling, and test structure that future agents will use.

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/)

## Getting started

Install the project and its development dependencies:

```bash
uv sync --dev
```

Run the test suite:

```bash
uv run pytest
```

Check code quality:

```bash
uv run ruff check .
uv run ruff format --check .
```

## Project structure

```text
creator-os/
├── docs/                 # Architecture and product documentation
├── scripts/              # Development and operational scripts
├── src/creator_os/       # Installable Python package
├── tests/                # Automated tests
├── pyproject.toml        # Project metadata and tool configuration
└── uv.lock               # Reproducible dependency lock file
```

## Roadmap

- Trend Agent (core ranking engine complete; live source pending)
- Creator Memory
- Prompt Compiler
- Content workflow orchestration

## Development principle

Keep modules small, typed, and independently testable. External services should
be integrated behind explicit interfaces so that the core remains easy to test.
