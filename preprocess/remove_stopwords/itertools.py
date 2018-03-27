import itertools
import re

''' Utility function to clean tweet, remove repeated chars'''
def improve_repeated(text):
    text = ''.join(''.join(s)[:2] for _, s in itertools.groupby(text))
    print(text)
    return text 

def remove_url(text):
    mypatt = "http[s]?://[a-zA-Z0-9]*"
    strongpatt = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(strongpatt, text)
    f = 0
    for url in urls:
        i = text.index(url)
        text = text[:i] + text[i+len(url):]
    return text

def split_words(text):
	ans = ""
	for a in re.findall('[A-Z][^A-Z]*', text):
		ans+=a.strip()+' '
	return ans


text = "President Duterte PrayForMarawi PrayForPhilippines PrayForTheWorldhttps://"
print(text)
text = split_words(text)
print(text)
text = remove_url(text)
print(text)
text = improve_repeated(text)
print(text)
