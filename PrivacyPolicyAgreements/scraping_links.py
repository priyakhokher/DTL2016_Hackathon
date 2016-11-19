#!usr/bin/env/python2
# -*- coding: utf-8 -*-

import os
import sys
from bs4 import BeautifulSoup
import urllib
import csv
import nltk

if __name__ == '__main__':
	company = []      # list for appending name of the companies
	privacy_terms_url = []  # list for appending the urls
	with open ("Links.txt",'r') as file:
		for index,line in enumerate(file.readlines()) :
			# read the even lines into company and odd lines as their privacy term url 
			if index%2==0:
				company.append(line.strip())
			else:
				privacy_terms_url.append(line.strip())

	# print company
	# print privacy_terms_url


	for url in privacy_terms_url[1:2]:
		r = urllib.urlopen(url).read()
		soup = BeautifulSoup(r,"lxml")
		lists = soup.find_all("li")


	for k in lists[:15]:
		print k
		markup = str(k)
		soup = BeautifulSoup(markup,'lxml')
		print soup.get_text().encode("utf-8")
		print 
		break

	


		

	