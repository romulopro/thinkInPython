# -*- coding: utf-8 -*-
'''
Created on 1 de nov de 2018

@author: Romulo
'''
import os
from site import abs_paths
import hashlib
dict_of_md5 = {}

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def search_files_for_type(absolute_path = "H:\\Downloads", extension = 'mp3'):
    for path in os.listdir(absolute_path):
        roots_path = os.path.join(absolute_path + "\\" + path)
        if os.path.isdir(roots_path):
            search_files_for_type(roots_path , extension)
        else:
            if roots_path[-3:] == extension:
                md5_file = md5(roots_path)
                if is_a_duplicate_files(md5_file):
                    print("Arquivo duplicado:\n" + dict_of_md5[md5_file] + "\n" + path + "\n.........")
                else:
                    dict_of_md5[md5_file] = path
            
    return

def is_a_duplicate_files(md5_file):
    if dict_of_md5.__contains__(md5_file):
        return True
    return False
    
    
if __name__ == '__main__':
    '''print(os.getcwd())
    for path in os.listdir(os.getcwd()):
        print(path)'''
    
    search_files_for_type("H:\\Músicas", 'jpg')
    #is_a_duplicate_files()
    print()
    
    