# -*- coding: utf-8 -*-

from polyglot.detect import Detector

text = "# PrayForMarawi"
# detector = Detector(text.decode('utf-8'), quiet = True).languages
# print(detector.language)

#----------------------------------------------------------------------
def detect_english(tweet):
	languages = Detector(tweet.decode('utf-8'), quiet=True).languages
	for language in languages:
		if language.name == "English":
			print(language.confidence)
			if float(language.confidence) >= 85.0:
				return True
			else:
				return False
	return False

english = detect_english(text)
print(english)