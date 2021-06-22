# docx_search

A python library built to search for keywords in .docx files.

## Disclaimer

The code works (On windows at least). But it isn't pretty. (actually really messy...) If you wan't to clean it up, Feel free to do so.

## Installation

There isn't a release to pypi yet, and i am still making changes to the code.

To use the library, move the "docx_search" folder into your project.

## Usage

```python
import docx_search

docx_search.run('Keyword', 'Path\\to\\file') # Returns a list with files that contain the keyword.

```

NOTE! The Keyword is case sensitive. And remember tu use double backslashes in the file path as python sees a single backslash as an escape marker.

## License

This project is licensed under the GNU GPLv3 License. See [LICENSE](LICENSE "LICENSE")
