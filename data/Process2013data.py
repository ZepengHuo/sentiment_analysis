import re
import numpy as np
import itertools
from collections import Counter
import twokenize


def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    # string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    # string = re.sub(r"\'s", " \'s", string)
    # string = re.sub(r"\'ve", " \'ve", string)
    # string = re.sub(r"n\'t", " n\'t", string)
    # string = re.sub(r"\'re", " \'re", string)
    # string = re.sub(r"\'d", " \'d", string)
    # string = re.sub(r"\'ll", " \'ll", string)
    # string = re.sub(r",", " , ", string)
    # string = re.sub(r"!", " ! ", string)
    # string = re.sub(r"\(", " \( ", string)
    # string = re.sub(r"\)", " \) ", string)
    # string = re.sub(r"\?", " \? ", string)
    # string = re.sub(r"\s{2,}", " ", string)
    string = twokenize.tokenizeRawTweetText(string)
    string = " ".join(str(x) for x in string)
    return string.strip().lower()

pos=open("./2013 data/rt-polarity.pos",'a+')
neg=open("./2013 data/rt-polarity.neg",'a+')


with open("2013_taskB.tsv") as f0:
    for line in f0:
        try:
            line=clean_str(line) 
        except:
            pass
        line=line.split()
        #print line
        if line[3]=='positive':    #with tokenized, it's 3. not, 2
            for word_index in range(5,len(line)):   #with tokenized, it's 5. not, 3
                if len(line[word_index])>3 and line[word_index][0:4] == 'http':
                    pass;
                else:
                    pos.write(line[word_index])
                    pos.write(' ')
            pos.write('\n')
        elif line[3]=='negative':    #with tokenized, it's 3. not, 2
            for word_index in range(5,len(line)):    #with tokenized, it's 5. not, 3
                if len(line[word_index])>3 and line[word_index][0:4] == 'http':
                    pass;
                else:
                    neg.write(line[word_index])
                    neg.write(' ')
            neg.write('\n')
pos.close()
neg.close()