train_data=[]
train_labels=[]
with open('downloaded_A_train.tsv') as f:
        for line in f:
            line=line[:-1]
            if line[19:22]=='neg' or line[19:21]=='pos':
                train_data.append(line[28:])
                train_labels.append('non-neu')
            elif line[19:22]=='neu':
                train_data.append(line[27:])
                train_labels.append('neu')
print train_data