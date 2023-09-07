# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2023-09-07

### Added

- Initial release of `json-to-ndjsonify`.
- Implemented core logic for converting JSON files with a specified node (default is 'edges') to NDJSON format.
- Included CLI for ease of use.
- Added support for providing an input file and target node via command-line parameters (`--input` and `--node`).
- Created a README with detailed usage and configuration instructions.
- Unit tests for verifying the validity of generated NDJSON files.
- Basic package structure with `setup.py` for package installation.
