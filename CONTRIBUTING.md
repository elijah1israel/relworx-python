# Contributing to Relworx Python SDK

Thank you for your interest in contributing! Here's how to get started.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/relworx-python.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
5. Install dev dependencies: `pip install -e ".[dev,test]"`

## Making Changes

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Write or update tests
4. Run tests: `pytest`
5. Format code: `black .`
6. Sort imports: `isort .`
7. Lint: `flake8 src/relworx tests`
8. Type check: `mypy src/relworx`

## Submitting Changes

1. Commit with clear messages: `git commit -m "Add feature X"`
2. Push to your fork: `git push origin feature/your-feature`
3. Open a Pull Request with a description of your changes

## Code Style

- Use [Black](https://black.readthedocs.io/) for formatting
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Add type hints to all functions
- Write docstrings for all public functions

## Testing

- Add tests for any new functionality
- Aim for >80% code coverage
- Use pytest and requests-mock for API testing

## Reporting Issues

- Use GitHub Issues for bug reports
- Include Python version, SDK version, and error traceback
- Provide a minimal example to reproduce the issue

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
