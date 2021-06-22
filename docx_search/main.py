# -*- coding: utf-8 -*-
import os
import zipfile
import shutil as sh

org = []
end = []

def index(search_path):
    if os.path.exists('index.txt'):
        os.remove('index.txt')
    numberoffiles = 0
    for root, dir, files in os.walk(search_path):
        result = files
        roots = root
        for a in files:
            write(root + '\\' + a)
            numberoffiles += 1
    write('\n' + str(numberoffiles))

def write(line):
    if '~$' not in line:      
        with open('index.txt', 'a') as f:
           f.write(line)
           f.write('\n')

def search_filetype(filetype):
    searchfile = open("index.txt", "r")
    a_list = []
    for line in searchfile:
        if '.' + filetype in line: 
            a_list.append(line)
    searchfile.close()
    nil = len(a_list)
    counter = 0
    while counter < nil:
        a_list[counter] = a_list[counter][:-1]
        counter += 1
    return a_list

def unzip(path_to_file, dir, counter):
    org.append(path_to_file)
    end.append('unzip\\' + str(counter))
    if os.path.isdir('unzip') == False:
        os.mkdir('unzip')
    sh.copyfile(path_to_file, end[counter] + '.zip')
    with zipfile.ZipFile(end[counter] + '.zip') as zip_ref:
        zip_ref.extractall(dir)
    sh.copyfile(dir + '\\word\\document.xml', dir + '\\document.xml')

def search(kewyord, file):
    searchfile = open(file, "r")
    a_list = []
    for line in searchfile:
        if kewyord in line: 
            a_list.append(file)
            found = file
    searchfile.close()
    if len(a_list) > 0:
        counter = 0
        while counter < len(end):
            if end[counter] + '\\document.xml' == found:
                found = str(org[counter])
            counter += 1
        return found


# Try.py
def run(keyword, s_path):
    index(s_path)
    response = []
    a_list = search_filetype('docx')
    nil = len(a_list)
    counter = 0
    indexv = []
    foundin = []
    while counter < nil:
        unzip(a_list[counter], 'unzip\\' + str(counter), counter)
        indexv.append('unzip\\' + str(counter) +  '\\document.xml')
        counter += 1
    nili = len(indexv)
    counter = 0

    while counter < nili:
        respons = str(search(keyword, indexv[counter]))
        if respons != 'None':
            response.append(respons)
        counter += 1
    
    try:
        sh.rmtree('unzip')
    except:
        pass

    return response
