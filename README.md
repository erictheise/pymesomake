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

```
python pymesomake --sourcefile='data/genesis.txt' --mesostring="these are the times that try men's souls"
```


### Reminder to Maintainer

Publish thusly:

```
$ python3 setup.py sdist bdist_wheel
$ twine updload dist/*
```

### Acknowledgements & Resources

Andrew Culver

* [post to silence mailing list](https://lists.virginia.edu/sympa/arc/silence/2019-01/msg00013.html) that inspired this code
* compilation of [computer programs used by John Cage](http://www.anarchicharmony.org/People/Culver/CagePrograms.html)
  
The Holy See

* [source of Genesis text](http://www.vatican.va/archive/bible/genesis/documents/bible_genesis_en.html). HTML source subjected to these minimal edits:
    * removal of page navigation elements
    * removal of chapter headings (e.g., "Chapter 6") and line numbering (e.g., "[1:30]")
    
    
Marjorie Perloff contextual essays

* [John Cage Conceptualist Poet](http://thebatterseareview.com/critical-prose/116-john-cage-conceptualist-poet)
* [The Music of Verbal Space: John Cage’s “What You Say”](http://marjorieperloff.com/essays/cage-verbal-space/)
