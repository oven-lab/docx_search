# docx_search

A python library built to search for keywords in .docx files.

## Installation

### Easy:

`pip install docx_search`

### Advanced:

Requires git.

`Git clone https://github.com/WaldemarBjornstrom/docx_search`

Then place the downloaded files in your project.

## Usage

```python
import docx_search

docx_search.run('Keyword', 'Path\\to\\file') # Returns a list with files that contain the keyword.
docx_search.run('Keyword', 'Path\\to\\file', encoding='utf-8') # Returns a list with files that contain the keyword, with encoding = 'utf-8'

```

NOTE! The Keyword is case sensitive. And remember tu use double backslashes in the file path as python sees a single backslash as an escape marker.

## License

This project is licensed under the GNU GPLv3 License. See [LICENSE](LICENSE "LICENSE")
