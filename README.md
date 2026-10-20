# LeakCheck.io Searcher

A lightweight Python CLI tool by NexForm3D for querying the LeakCheck public API and displaying data exposure search results.

## Features

- Search using a username or email address
- Display result fields and associated source information
- Colored terminal interface
- Optional export of search metadata to a text file
- Request timeout and error handling

## Requirements

- Python 3.10 or newer
- Access to the LeakCheck public API

## Installation

Clone the repository:

```bash
git clone https://github.com/Nexform-star/LeakCheck.io-Searcher.git
cd LeakCheck.io-Searcher
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python leakcheck.py
```

Enter a username or email address when prompted. Follow the instructions displayed in the terminal to view the results or export the search metadata.

## Dependencies

- [Requests](https://pypi.org/project/requests/) for HTTP requests
- [Colorama](https://pypi.org/project/colorama/) for terminal colors
- [fade](https://pypi.org/project/fade/) for terminal text effects

## Responsible Use

This project is intended for educational purposes and authorized personal security checks.

- Only search for information you own or are authorized to investigate.
- Do not use the tool to expose private information or target other people.
- Search results may be incomplete or inaccurate.
- Do not commit credentials, API keys, or sensitive search results to the repository.

## Disclaimer

This project is an independent tool and is not affiliated with or endorsed by LeakCheck. API availability and response formats may change.

Users are responsible for complying with applicable laws, API terms, and the rights of others.

## License

See the repository's license file for licensing terms.
