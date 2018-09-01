# tinyurl-python
[![Build Status](https://travis-ci.org/gaborantal/TinyURL-Python.svg?branch=master)](https://travis-ci.org/gaborantal/TinyURL-Python)
Python module to create short links with tinyurl.com

# Installation
```sh
git clone https://github.com/gaborantal/TinyURL-Python.git
```
```sh
cd TinyURL-Python
```
```sh
python setup.py install
```

# Usage
```py
>>> import tinyurl
```
```py
>>> print tinyurl.shorten("www.abc.com", "xyz")
>>> http://www.abc.com/xyz
```
```py
>>> print tinyurl.shorten("www.abc.com")
>>> http://www.abc.com/wxghf
```
Here, tinyurl has shorten function which takes two parameters. First is URL which you want to short and second one is custome name.
Do not pass any second argument if you want a random alias.
