## PyMesomake

PyMesomake is a Python 3 implementation of the mesostic generation algorithm Andrew Culver developed for John Cage.


## Installation

### Windows

I only use Windows for testing in my projects but these instructions work for me on a vanilla Windows 10 VirtualBox virtual machine:

0. If you don't already have Python on your system download and install the current release from [python.org](https://www.python.org/). 

1. Open a Command Prompt.
 
2. Run this command.

```python
pip install pymesomake
```

3. Download the `punkt` tokenizer from Python's Natural Language Tool Kit.

```
python -m nltk.downloader punkt
```
4. Download [this file, containing the text of Genesis](https://raw.githubusercontent.com/erictheise/pymesomake/master/data/genesis.txt).


5. Run this command, making sure to provide the correct path to the downloaded Genesis text.

```
python -m pymesomake --sourcefile=Downloads\genesis.txt --mesostring="these are the times that try men's souls"
```

You should see a mesostic on your screen. Congratulations.


### MacOS

_coming soon_

### Linux

_coming soon_


## Usage

```
python pymesomake --sourcefile='data/genesis.txt' --mesostring="these are the times that try men's souls"
```


## Reminder to Maintainer

Publish thusly:

```
python setup.py sdist bdist_wheel
twine upload dist/*
```

## Acknowledgements & Resources

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
