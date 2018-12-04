#!/usr/bin/python3

import sys
import re


def line_decode(line,encoding='ascii'):
    '''
    The function returns string in ASCII encoding 
    :param line: bytes type
    :param encoding: ASCII encoding as default
    :return: decoded line in ASCII without end symbol r'\n'
    '''
    res= line.decode(encoding=encoding,errors='replace')
    return res[:-1] 

def string_processing(line):
    '''
    The function splits line in parts containing only word's symbols (see re module)
    :param line: string in ASCII encoding
    '''
    res = re.split(r'[\W]+',line,flags=re.ASCII)
    return res


def max_length_words(words):
    '''
    The function-generator that returns keys(words) of max value(length) from sorted on values dict  
    :param words: list like [(word,len(word)),...]
    '''
    l=sorted(words,key=(lambda x: x[1]),reverse=True) # sorted list of (word(key),length(value))
    if not l:
        raise StopIteration()
    l=dict(l)                                         # dict from sorted list to remove same keys
    prev_value=-1
    for k in l:                                       # return only max values keys 
        if l[k]<prev_value:                           
            break                                       
        else:
            prev_value=l[k]
            yield (k,l[k])
    #raise StopIteration()

def main(InputFile=sys.stdin,OutputFile=sys.stdout,argv=sys.argv):
    '''
    The function reads InputFile in byte mode,
    decodes lines in ASCII splitting them
    into separate words(keys) and writes
    words of max length(value) in OutputFile 
    each line of that contains key\\tvalue
    :param InputFile: file object that should be opened for reading
    :param OutputFile: file object that should be opened for writing
    :param argv: not used
    '''
    for line in InputFile.buffer: #reading raw lines
        if len(line)==1:          #strings like '\n' are skipped
            continue
        DecodedLine = line_decode(line)   #decoding line in ASCII           
        Keys = string_processing(DecodedLine) # spliting line in keys
        for (key,value) in max_length_words( \
            zip(map(lambda x: x.lower(),Keys),map(lambda x: len(x),Keys))): 
            OutputFile.write(key+'\t'+str(value)+'\n')


if __name__ == "__main__":
    main()