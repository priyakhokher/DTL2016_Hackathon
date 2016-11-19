#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

markup = '<li>\n<span class="a-list-item"><a href="#GUID-1B2BDAD4-7ACF-4D7A-8608-CBA6EA897FD3__SECTION_467C686A137847768F44B619694D3F7C"> What Personal Information About Customers Does Amazon.com Gather?</a></span>\n</li>'
soup = BeautifulSoup(markup,'lxml')

print soup.get_text()
# u'\nI linked to example.com\n'
soup.i.get_text()
#u'example.com'