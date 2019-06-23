 # -*- coding: utf-8 -*-

import string
def sed(pattern_string, replacement_string, source_file, destination_file):
    try:
        fread = open(source_file, 'r')
    except IOError:
        print("file doesn't exist")
        return
    fwrite = open(destination_file, 'w')
    for line in fread:
        line_to_write = ""
        for word in line:
            if word is pattern_string:
                line_to_write = line_to_write + replacement_string
            else:
                line_to_write = line_to_write + word
        fwrite.write(line_to_write)
    fread.close()
    fwrite.close()
    
    return

        

if __name__ == '__main__':
    sed('I', 'DEFF', 'tale1.txt', 'talemod.txt')   