#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import urllib.request


def shorten(long_url, alias=None):
    url = ("http://tinyurl.com/create.php?source=indexpage"
           "&url={url}"
           "&submit=Make+TinyURL%21".format(url=long_url))
    if alias:
        url += "&alias={alias}".format(alias=alias)
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    check_error = soup.p.b.string
    if "The custom alias" in check_error:
        return "Alias you have selected is already used by someone else."
    else:
        return soup.find_all('div', {'class': 'indent'})[1].b.string
