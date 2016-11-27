import re
import numpy as np
import itertools
from collections import Counter
import twokenize

#only put downloaded_A_train.tsv into one file, can put more


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



p=open('rt-polarity.dev.pos','a+')
n=open('rt-polarity.dev.neg','a+')
#neu=open('rt-polarity.dev.neu','a+')
with open("downloaded_A_dev.tsv", 'r') as f0:
    for line in f0:
        line=clean_str(line) 
        line=line.split()
        if line[1] == 'positive':
            #write when available
            if line[2] != 'not' and line[3] != 'available':
                for word_index in range(2,len(line)):
                    if len(line[word_index])>3 and line[word_index][0:4] == 'http':
                        pass;
                    else:
                        #line[word_index]=re.sub('([@#$%^&*+={}:;<>~`".,!?()])', r' \1 ', line[word_index])
                        #line[word_index]=re.sub('\s{2,}', ' ', line[word_index])
                        p.write(line[word_index])
                        p.write(' ')
                p.write('\n')
        elif line[1] == "negative":
            #write when available
            if line[2] != 'not' and line[3] != 'available':
                for word_index in range(2,len(line)):
                    if len(line[word_index])>3 and line[word_index][0:4] == 'http':
                        pass;
                    else:
                        #line[word_index]=re.sub('([@#$%^&*+={}:;<>~`".,!?()])', r' \1 ', line[word_index])
                        #line[word_index]=re.sub('\s{2,}', ' ', line[word_index])
                        n.write(line[word_index])
                        n.write(' ')
                n.write('\n')
        '''if line[1] == 'neutral':
            #write when available
            if line[2] != 'not' and line[3] != 'available':
                for word_index in range(2,len(line)):
                    if len(line[word_index])>3 and line[word_index][0:4] == 'http':
                        pass;
                    else:
                        #line[word_index]=re.sub('([@#$%^&*+={}:;<>~`".,!?()])', r' \1 ', line[word_index])
                        #line[word_index]=re.sub('\s{2,}', ' ', line[word_index])
                        neu.write(line[word_index])
                        neu.write(' ')
                neu.write('\n')
            '''
            
            
            
            
p.close()
n.close()
#neu.close()