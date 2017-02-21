# -*- coding: utf-8 -*-
import os,sys
from lxml.html import fromstring as fs
from lxml.html.clean import Cleaner

cleaner = Cleaner()
cleaner.javascript = True
cleaner.style = True
cleaner.scripts = True
pathSave =  os.path.join(os.getcwd(),"plaintext.txt")

def htmlParser(htmlfile):
        text = cleaner.clean_html(fs(htmlfile)).text_content()
        text2save = text.replace("\n"," ")+"\n"
        with open(pathSave,'a',encoding='utf-8') as file2save:
                file2save.write(text2save)


if __name__ == "__main__":
        path = "./HTML"
        for htmlName in os.listdir(path):
                filePath = os.path.join(os.getcwd(),"HTML",htmlName)
                if os.path.isfile(filePath) and filePath[-1] != "~":
                        print(filePath)
                        with open(filePath,'r',encoding='utf-8') as theFile:
                                htmlParser(theFile.read())
