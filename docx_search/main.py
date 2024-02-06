# -*- coding: utf-8 -*-
import os
import shutil as sh
import zipfile
import re
from pathlib import Path

#include progress bar
from ipywidgets import IntProgress
from IPython.display import display
import time


org, end, response, indexv = [], [], [], []

def findtag(line, tag):
    reso = ""
    reg_str = "<" + tag + ">(.*?)</" + tag + ">"
    res_str = '<w:t xml:space="preserve">(.*?)</w:t>'
    res = re.findall(reg_str, line)
    reg = re.findall(res_str, line)
    for i in res:
        reso += i
    for i in reg:
        reso += i
    return reso

def run(keyword, s_path, encoding=None):
    if os.path.exists('index.txt'):
        os.remove('index.txt')
    numberoffiles = 0
    for root, dir, files in os.walk(s_path):
        result = files
        roots = root
        for a in files:
            if '~$' not in root + '\\' + a:      
                with open('index.txt', 'a', encoding=encoding) as f:
                    extension = Path(a).suffix
                    
                    #only consider the .doc and .docx files
                    if ((extension == '.doc') or (extension == '.docx')):
                        f.write(root + '\\' + a)
                        f.write('\n')

    searchfile = open("index.txt", "r", encoding=encoding)
    a_list = []
    for line in searchfile:
        if '.' + 'docx' in line: 
            a_list.append(line)
    searchfile.close()
    counter = 0
    while counter < len(a_list):
        a_list[counter] = a_list[counter][:-1]
        counter += 1

    
    f = IntProgress(min=0, max=len(a_list), description="loading files:") # instantiate the progress bar
    display(f) # display the progress bar
    
    counter = 0
    while counter < len(a_list):
        org.append(a_list[counter])
        end.append('unzip\\' + str(counter))
        if os.path.isdir('unzip') == False:
            os.mkdir('unzip')
        sh.copyfile(a_list[counter], end[counter] + '.zip')

        try:   #in case there are some doc/docx that cannot be opened as zip
            with zipfile.ZipFile(end[counter] + '.zip') as zip_ref:
                zip_ref.extractall('unzip\\' + str(counter))
            sh.copyfile('unzip\\' + str(counter) + '\\word\\document.xml', 'unzip\\' + str(counter) + '\\document.xml')
            indexv.append('unzip\\' + str(counter) +  '\\document.xml')
        except Exception as e:
            if e == "File is not a zip file":
                continue
        
        counter += 1
        f.value = counter   #update progress bar

    

    f = IntProgress(min=0, max=len(indexv), description="scanning files:") # instantiate the progress bar
    display(f) # display the progress bar

    counter = 0
    while counter < len(indexv):
        searchfile = open(indexv[counter], "r", encoding=encoding)
        a_list = []
        for line in searchfile:
            var = findtag(line, 'w:t')
            if keyword in var: 
                a_list.append(indexv[counter])
                found = indexv[counter]
        searchfile.close()
        if len(a_list) > 0:
            counterr = 0
            while counterr < len(end):
                if end[counterr] + '\\document.xml' == found:
                   found = str(org[counterr])
                counterr += 1

            respons = str(found)
        else:
            respons = 'None'

        if respons != 'None':
            response.append(respons)       
            
        counter += 1     
        f.value = counter   #update progress bar
    
    try:
        sh.rmtree('unzip')
        os.remove('index.txt')
    except:
        pass
    
    return response
