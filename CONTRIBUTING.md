# Contributing to JSON To Ndjsonify

## Introduction

Thank you for considering contributing to JSON to NDJSONify. This document outlines the process and guidelines for contributing. We value your input, be it in the form of bug reports, feature requests, or code contributions.

## Workflow

This project adheres to the Git Flow workflow for managing changes. For those unfamiliar, Git Flow is a set branching model for Git that defines a structured release flow and feature development. Below are the key points:

- `master`: The production-ready state of your code.
- `develop`: The main branch where the latest developments occur. All branching should start from here.
- `feature/`: A branch for developing a new feature. Always branch off from `develop`.
- `hotfix/`: Quick fixes for issues that are urgent and cannot wait for the next release.
- `release/`: Preparing new production releases. Integrate feature branches and bug fixes and get ready for a merge into `master`.

### Steps

1. Fork the repository and clone it locally.
2. If you are contributing a feature, create a new branch from `develop` with a descriptive name like `feature/new-api-endpoint`.
3. Make your changes, commit them, and push the branch.
4. Make a Pull Request to merge your feature branch into the `develop` branch of the original repository.
5. Once reviewed and approved, the maintainers will merge your changes.

By sticking to this workflow, we maintain a clean and easily understandable commit history, and also manage releases in a structured manner.

## Commit and Versioning Guidelines

### Semantic Commit Messages

To make the commit history more readable and useful, we follow the Semantic Commit Messages format. The format is as follows:

```
<type>(<scope>): <short summary>
  │       │             │
  │       │             └─> Summary in present tense. Not capitalized. No period at the end.
  │       │
  │       └─> Commit Scope: feature, bugfix, improvement, etc.
  │
  └─> Commit Type: build, chore, ci, docs, style, refactor, perf, test
```

For example:

- `feat(button): add a disabled state`
- `fix(input): resolve the validation error`
- `chore: update dependencies`

This makes it easier to browse the history, revert changes, or understand what a commit does just by looking at its message.

### Semantic Versioning

This project adheres to Semantic Versioning. Given a version number MAJOR.MINOR.PATCH, we increment:

- `MAJOR` version when making incompatible API changes,
- `MINOR` version when adding functionality in a backward-compatible manner, and
- `PATCH` version when making backward-compatible bug fixes.

For more information, please refer to [Semantic Versioning](https://semver.org/).

## Development Environment

Please make sure you have the following software installed:

- Python 3.x
- Git

## Code Standards

- Follow PEP 8 for Python code.
- Type annotate functions and methods.
- Write meaningful commit messages.

## Testing

Before submitting a pull request, please run the unit tests to ensure that your changes have not broken any existing functionality.

```bash
export NDJSON_DIR=/path/to/your/ndjson/directory
python -m unittest tests/test_main.py
```

## Submitting Changes

1. Push your changes to your forked repository.
2. Create a pull request from your fork to the main repository.
3. In the pull request description, explain your changes and how they benefit the project.

## Review Process

Once your pull request is submitted:

1. Project maintainers will review your code.
2. Address any comments or feedback from the maintainers.
3. Once approved, your pull request will be merged.

## License

By contributing to JSON to NDJSONify, you agree to comply with the project's [LICENSE](LICENSE).
