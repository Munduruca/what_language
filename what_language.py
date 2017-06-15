#you need to install nltk first, right?
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords

def what_language(answer):
	matches = {}
	answer_tokens = wordpunct_tokenize(answer)
	list_of_lower_tokens = [i.lower() for i in answer_tokens]

	for language in stopwords.fileids():
		stopwordss = set(stopwords.words(language))
		words = set(list_of_lower_tokens)
		intersections = words.intersection(stopwordss)
	
		matches[language] = len(intersections)
	
	most_matched_language = max(matches, key=matches.get)

	return most_matched_language



#a = 'this is my house'
#a = 'det här är mitt hus'
#a = 'cette maison la cest a moi'
#a = 'aquela e minha casa'
#a = 'mi casa su casa'
#a = 'du är så vacker'
a = '''
hej, hur mår du?
du är bäst kompis
din näsa är riktigt stor
hoppas du mår bra
'''

a = 'eu gosto de annaboy'


b = what_language(a)
print(type(b))
print(b.__dict__)