import gensim
from gensim.summarization import summarize
from gensim.summarization import keywords


print '\nage\n'
with open("FBAgreement.txt") as file:
	text = file.readlines()
	#text = ''.join(text)
	age_list = ['age','age-based','eligibility','eligible']
	age = map(lambda x: x if any(a in x.split(" ") for a in age_list) else None,text)
	age = filter(lambda x: x!=None,age)
	if len(age)<2:

		print age
	else:
		age_string = ''.join(age)
		print summarize(age_string)
	
	print '\nprivacy\n'
	privacy = ["privacy",'private','confidential','confidentiality']
	pr = map(lambda x: x if any(a in x.split(" ") for a in privacy) else None,text)
	pr = filter(lambda x: x!=None,pr)
	privacy_string = ''.join(pr)
	print summarize(privacy_string)
	print 
	print '\nwhat data is collected\n'
	data = ['data','content','provide','collected','given by you','given to us','obtained']
	my_information = map(lambda x: x if any(a in x.split(" ") for a in data) else None,text)
	my_information = filter(lambda x: x!=None,my_information)
	my_information_string = ''.join(my_information)
	print summarize(my_information_string)
	
	print '\nwhat is done with that data\n'
	data_used = ['data','content','used','use','share','shared','collected','third-party','third','party','advertisements','advertisement','ad','ads']
	shared = map(lambda x: x if any(a in x.split(" ") for a in data_used) else None,text)
	shared = filter(lambda x: x!=None,shared)
	shared_string = ''.join(shared)
	print summarize(shared_string)
	
	
	print '\nare cookies used ?\n'
	cookies = filter(lambda x: 'cookies' in x.split(" "), text)
	cookies_string = ''.join(cookies)
	print summarize(cookies_string)

	print '\n Conflicts\n'
	conflicts = filter(lambda x: 'conflict' in x.split(" "), text)
	conflicts_string = ''.join(conflicts)
	print summarize(conflicts_string,ratio=0.5)







