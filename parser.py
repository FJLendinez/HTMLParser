# -*- coding: utf-8 -*-
import os,sys
from lxml.html import fromstring as fs
from lxml.html.clean import Cleaner

cleaner = Cleaner()
cleaner.javascript = True
cleaner.style = True
cleaner.scripts = True
pathSave =  os.path.join(os.getcwd(),"plaintext.txt")

def cleanText(text):
        data = text.split()
        t = ""
        for d in data:
                t +=d+" "
        t = t[:-1]+"\n\n"
        return t

def htmlParser(htmlfile):
        text = cleaner.clean_html(fs(htmlfile)).text_content()
        textReplaced = text.replace("\n"," ").replace("\t"," ")
        text2save = cleanText(textReplaced)
        with open(pathSave,'a',encoding='utf-8') as file2save:
                file2save.write(text2save)

def searchFile(path):
    for f in os.listdir(path):
        filePath = os.path.join(path,f)
        if os.path.isfile(filePath) and filePath[-1] != "~":
            print(filePath)
            with open(filePath,'r',encoding='utf-8',errors='surrogateescape') as theFile:
                htmlParser(theFile.read().strip())
        elif os.path.isdir(filePath):
            searchFile(filePath)

if __name__ == "__main__":
        filePath = os.path.join(os.getcwd(),"HTML")
        searchFile(filePath)
