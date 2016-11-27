c0_pos=open('./Cluster 0/rt-polarity.pos','a+')
c0_neg=open('./Cluster 0/rt-polarity.neg','a+')
c1_pos=open('./Cluster 1/rt-polarity.pos','a+')
c1_neg=open('./Cluster 1/rt-polarity.neg','a+')
c2_pos=open('./Cluster 2/rt-polarity.pos','a+')
c2_neg=open('./Cluster 2/rt-polarity.neg','a+')


with open("clustering_OUTPUT.txt") as f0:
    for line in f0:
        if line[9] == '0':
            if line[0:3] == 'pos':
                c0_pos.write(str(line[12:]))
            elif line[0:3] == 'neg':
                c0_neg.write(str(line[12:]))
        elif line[9] == '1':
            if line[0:3] == 'pos':
                c1_pos.write(str(line[12:]))
            elif line[0:3] == 'neg':
                c1_neg.write(str(line[12:]))
        elif line[9] == '2':
            if line[0:3] == 'pos':
                c2_pos.write(str(line[12:]))
            elif line[0:3] == 'neg':
                c2_neg.write(str(line[12:]))