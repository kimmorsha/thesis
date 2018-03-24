import os

""" 
Renames the filenames within the same directory to be Unix friendly
(1) Changes spaces to hyphens
(2) Makes lowercase (not a Unix requirement, just looks better ;)
Usage:
python rename.py
"""

path =  os.getcwd()
filenames = os.listdir(path)

print(path)
num = 2

for filename in filenames:
	print(filename)
	if num < 10:
		new_filename = "marawi_tweets_09_0" + str(num) + ".csv"
		os.rename(filename, new_filename)
		num = num + 1
	elif num == 5 or num == 6 or num == 7 or num == 8 or num == 9 or num == 10 or num == 15 or num == 16 or num == 17:
		pass
	else:
		new_filename = "marawi_tweets_09_" + str(num) + ".csv"
		os.rename(filename, new_filename)
		num = num + 1
	
