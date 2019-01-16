## PyMesomake

PyMesomake is a Python 3 implementation of the mesostic generation algorithm Andrew Culver developed for John Cage.


### Installation

Unless you've previously used Python's Natural Language Tool Kit you'll see this error on your first run of `PyMesomake`.

```
LookupError: 
**********************************************************************
  Resource punkt not found.
  Please use the NLTK Downloader to obtain the resource:

  >>> import nltk
  >>> nltk.download('punkt')
  
  Attempted to load tokenizers/punkt/PY3/english.pickle

  Searched in:
    - '/Users/erictheise/nltk_data'
    - '/Users/erictheise/Repos/erictheise/venvs/pymesomake/nltk_data'
    - '/Users/erictheise/Repos/erictheise/venvs/pymesomake/share/nltk_data'
    - '/Users/erictheise/Repos/erictheise/venvs/pymesomake/lib/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
    - ''
**********************************************************************
```
You can download that component with:
```
$ python -m nltk.downloader punkt
[nltk_data] Downloading package punkt to
[nltk_data]     /Users/erictheise/nltk_data...
[nltk_data]   Unzipping tokenizers/punkt.zip.
$
```
### Usage

```python
python pymesomake/pymesomake.py --sourcefile='data/genesis.txt' --mesostring="these are the times that try men's souls"
```


### Acknowledgements

Andrew Culver
Vatican
Marjorie Perloff
