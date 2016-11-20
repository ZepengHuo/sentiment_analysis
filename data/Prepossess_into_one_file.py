import re

#only put downloaded_A_train.tsv into one file, can put more

f=open('all tweets in one file.txt','a+')
with open("downloaded_A_train.tsv", 'r') as f0:
    for line in f0:
        line=line.split()
        
        #write when available
        if line[2] != 'Not' and line[3] != 'Available':
            for word_index in range(2,len(line)):
                if len(line[word_index])>3 and line[word_index][0:4] == 'http':
                    break;
                else:
                    line[word_index]=re.sub('([@#$%^&*+={}:;<>~`".,!?()])', r' \1 ', line[word_index])
                    line[word_index]=re.sub('\s{2,}', ' ', line[word_index])
                    f.write(line[word_index])
                    f.write(' ')
            f.write('\n')
