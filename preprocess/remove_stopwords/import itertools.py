import itertools

''' Utility function to clean tweet, remove repeated chars'''
def improve_repeated(text):
    text = ''.join(''.join(s)[:2] for _, s in itertools.groupby(text))
    print(text)
    return text  

text = "soooooooo happyyyyyyy"

print(improve_repeated(text))
