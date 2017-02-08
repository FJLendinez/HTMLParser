# -*- coding: utf-8 -*-
import os, lxml,sys
from lxml.html.clean import Cleaner

cleaner = Cleaner()
cleaner.javascript = True 
cleaner.style = True 
cleaner.scripts = True
pathSave =  os.path.join(os.getcwd(),"plaintext.txt")

def htmlParser(htmlfile):
	text = cleaner.clean_html(lxml.html.fromstring(htmlfile)).text_content()
	text2save = text.replace("\n"," ")+"\n"
	file2save = open(pathSave,'a')
	file2save.write(str(text2save.encode(sys.stdout.encoding, errors='replace')))
	

if __name__ == "__main__":
	path = "./HTML"
	for htmlName in os.listdir(path):
		filePath = os.path.join(os.getcwd(),"HTML",htmlName)
		if os.path.isfile(filePath) and filePath[-1] != "~":
			print(filePath)
			theFile = open(filePath,'r').read()
			htmlParser(theFile)
