#-*- coding: utf-8 -*-

from polyglot.detect import Detector
import string

text = "Huhuhuhu please pray for marawi huwag magpakatanga tayo ay makibaka please duterte help us po"

# text = filter(lambda x: x in string.printable, text)
languages = Detector(text.decode('utf-8'), quiet=True).languages
is_english = False
max_confidence = 0
print(text)
for language in languages:
	print(language)
	# for language in languages:
	# 	if language.name == "English":
	# 		max_confidence = language.confidence
	# 		print(language.confidence)
	# 		if float(language.confidence) >= 93.0:
	# 			is_english = True
	# 		else:
	# 			is_english = False
	# 	else: 
	# 		if float(language.confidence) >= 50.0:
	# 			is_english = False
	# return is_english