#!/usr/bin/python3

import sys
from mapper import max_length_words


def main(InputFile=sys.stdin,OutputFile=sys.stdout,argv=sys.argv):
    '''
    The function reads InputFile and writes
    words of max length(value) in OutputFile 
    each line of that contains key\\tvalue
    :param InputFile: file object that should be opened for reading
    :param OutputFile: file object that should be opened for writing
    :param argv: not used
    '''
    words = map(lambda l: (l[0],(int(l[1]))),(line.split('\t') for line in InputFile))
    for word in max_length_words(words):
        OutputFile.write('{}\t{}\n'.format(*word))

if __name__ == "__main__":
    main()