#python example to infer document vectors from trained doc2vec model
import gensim.models as g
import codecs

#parameters
model="imdb1/model.bin"
test_docs="Testing pos+neg.txt"
output_file="imdb1/test_vectors(2).txt"

#inference hyper-parameters
start_alpha=0.01
infer_epoch=1000

#load model
m = g.Doc2Vec.load(model)
test_docs = [ x.strip().split() for x in codecs.open(test_docs, "r", "utf-8").readlines() ]

#infer test vectors
output = open(output_file, "w")
for d in test_docs:
    output.write( " ".join([str(x) for x in m.infer_vector(d, alpha=start_alpha, steps=infer_epoch)]) + "\n" )
output.flush()
output.close()