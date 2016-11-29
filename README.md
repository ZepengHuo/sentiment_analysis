# sentiment_analysis

Report files are stored in IEEE Conference folder, data and python codes are stored in data folder

How to see the result:

The data provided by Semeval is in downloaded_A_train.tsv, downloaded_A_devtest.tsv and downloaded_A_dev.tsv. Since devtest doesn't have label, we only use the other two

For data preprocessing part, the training data was processed into rt-polarity.train.txt file, then to create vector for each tweet, the file Doc2Vec_pretrained_WordEmbedding.py need to be run to train a model for word embedding. Due to the limitation of github, we can't upload the glove_model2.txt in the folder imdb1. But if this file can be downloaded and put into the imdb1 folder, then it can build the model of Doc2Vec. After that, It will genterate a file in imdb1 folder, the file's name is model.bin. Then, use infer_test.py to get the output vectors of each tweet using model.bin, stored as test_vectors.txt. For clustering, we need to run Clustering.py to get the centroids of each cluster, these centroids are stores in the file "three cluster centroids.txt". So when new testing data set comes, it first need to be run on infer_test.py to get the vectors stored in imdb1 folder, called test_vectors(2).txt, then it need to be decided which cluster it belongs to by using "Testing of Clustering.py", then it will assign 0, 1 or 2 to each tweet by checking the cosine similarity of each centroid and that vector.

The training folder and testing folder are results of preprocessing discussed above, and will be sent to CNN, to train and test, respectively. The training has three clusters, each cluster has two labeled datasets, positive and negative. The same as testing data set.

Since we already train the model and store it, thus you don't need to train our model again. 

By running the scitkit_svm_sentiment.py, you can see the result of baseline SVM

The data we feed to Tensorflow is stored in the folder call Training and Testing. In each folder we already have the clustered tweets stored in each folder. Inside each folder, we have rt-polarity.pos and rt-polarity.neg files, and they contains the tweets labeled as positive and negative, respectively.

The neural network part is in the link of Google drive. It will classify each cluster, and also classify all data together without clustering. In that part, we already trained the model too, so by only check the results (accuracy, precison, etc.), it only needs to run the eval.py to see the result.
