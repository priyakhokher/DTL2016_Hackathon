import gensim
from gensim.summarization import summarize
from gensim.summarization import keywords


with open("FBAgreement.txt") as file:
	text = file.readlines()
	text = ''.join(text)
	#print text
	print 'Keywords:'
	print keywords(text)