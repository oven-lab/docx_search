# -*- coding: utf-8 -*-
import os
import shutil as sh
import zipfile

org, end, response, indexv = [], [], [], []

def run(keyword, s_path):
    if os.path.exists('index.txt'):
        os.remove('index.txt')
    numberoffiles = 0
    for root, dir, files in os.walk(s_path):
        result = files
        roots = root
        for a in files:
            if '~$' not in root + '\\' + a:      
                with open('index.txt', 'a') as f:
                    f.write(root + '\\' + a)
                    f.write('\n')

    searchfile = open("index.txt", "r")
    a_list = []
    for line in searchfile:
        if '.' + 'docx' in line: 
            a_list.append(line)
    searchfile.close()
    counter = 0
    while counter < len(a_list):
        a_list[counter] = a_list[counter][:-1]
        counter += 1

    counter = 0
    while counter < len(a_list):
        org.append(a_list[counter])
        end.append('unzip\\' + str(counter))
        if os.path.isdir('unzip') == False:
            os.mkdir('unzip')
        sh.copyfile(a_list[counter], end[counter] + '.zip')
        with zipfile.ZipFile(end[counter] + '.zip') as zip_ref:
            zip_ref.extractall('unzip\\' + str(counter))
        sh.copyfile('unzip\\' + str(counter) + '\\word\\document.xml', 'unzip\\' + str(counter) + '\\document.xml')
        indexv.append('unzip\\' + str(counter) +  '\\document.xml')
        counter += 1

    counter = 0
    while counter < len(indexv):
        searchfile = open(indexv[counter], "r")
        a_list = []
        for line in searchfile:
            if keyword in line: 
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
    
    try:
        sh.rmtree('unzip')
        os.remove('index.txt')
    except:
        pass
    
    return response
