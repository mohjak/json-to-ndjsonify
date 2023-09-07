# JSON to NDJSONify

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Changelog](#changelog)
- [Contributing](#contributing)
- [License](#license)

## Overview

JSON to NDJSONify is a Python package specifically engineered for converting JSON files to NDJSON (Newline Delimited JSON) format. Built for developers who are working with APIs or data platforms that require NDJSON input, this package helps streamline your workflow by automating the conversion process.

## Features

- Supports complex nested JSON structures
- Ability to filter specific nodes (e.g., `edges`)
- Highly optimized and lightweight
- Written in Python, making it highly extensible and maintainable
- Unit tests to validate NDJSON output

## Installation

Clone the repository:

```bash
git clone https://github.com/mohjak/json_to_ndjsonify.git
```

Navigate to the cloned directory and run:

```bash
pip install .
```

Or directly via pip:

```bash
pip install json-to-ndjsonify
```

## Usage

### Basic Usage

To convert a JSON file to NDJSON:

```bash
json-to-ndjsonify --input sample.json --node edges
```

This will create an NDJSON file in the same directory as the `sample.json` file, suffixed with a timestamp.

### Advanced Usage

For additional configurations, consult the inline help:

```bash
json-to-ndjsonify --help
```

## Configuration

### Command-Line Parameters

- `--input`: Specifies the path of the JSON file to be converted.
- `--node`: Specifies the node name in the JSON file. Default is 'edges'.
- `--output`: Path to the output folder.

  Example:

  ```bash
  json-to-ndjsonify --input /path/to/your/file.json --node custom_edges --output /path/to/output/folder
  ```

## Running Tests

To execute the unit tests:

```bash
export NDJSON_DIR=/path/to/your/ndjson/directory
python -m unittest tests/test_main.py
```

## Changelog

See the [CHANGELOG.md](CHANGELOG.md) file for the latest changes in the current version.

## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md) file for how to contribute to this project.

## License

This package is licensed under the MIT License. See the `LICENSE.md` file for details.
