from scipy import spatial

c0_pos=open('./Cluster 0/rt-polarity.pos','a+')
c0_neg=open('./Cluster 0/rt-polarity.neg','a+')
c1_pos=open('./Cluster 1/rt-polarity.pos','a+')
c1_neg=open('./Cluster 1/rt-polarity.neg','a+')
c2_pos=open('./Cluster 2/rt-polarity.pos','a+')
c2_neg=open('./Cluster 2/rt-polarity.neg','a+')

three_centroids=[]
with open("three cluster centroids.txt") as f:
    one_centroid=[]
    for line in f:
        line=line.split()
        for item in line:
            if not item==']':
                if not item=='[':
                    one_centroid.append(float(item))
            elif item==']':
                three_centroids.append(one_centroid)
                one_centroid=[]

f1=open('Testing pos+neg.txt')
index=0
with open('./imdb1/test_vectors(2).txt') as f0:
    for line in f0:
        x=[]
        line=line.split()
        for item in line:
            item=float(item)
            x.append(item)
        three_sim=[]
        for centroid in three_centroids:
            #print len(three_centroids[1])
            three_sim.append(1-spatial.distance.cosine(x,centroid))
        cluster=three_sim.index(max(three_sim))
        if cluster==0:
            if index < 716:
                c0_pos.write(str(f1.readline()))
            elif index > 715:
                c0_neg.write(str(f1.readline()))
        if cluster==1:
            if index < 716:
                c1_pos.write(str(f1.readline()))
            elif index > 715:
                c1_neg.write(str(f1.readline()))
        if cluster==2:
            if index < 716:
                c2_pos.write(str(f1.readline()))
            elif index > 715:
                c2_neg.write(str(f1.readline()))
        index+=1