import sys, csv, numpy
#
space = 0.15
def classify(neighbors, point, train_X, pointsSet):
    sum = 0
    for j in neighbors:
        sum += train_X[j][-1]
    total = sum/len(neighbors)
    if(total >=.5):
        pointsSet[point] = 1
    else:
        pointsSet[point] = 0
    return pointsSet
        
#euclidean distance between 2 points
def eDist(newPoint, point):
    return numpy.linalg.norm(newPoint-point)
#k nearest neighbors for 1 new point
def get_nearest_neighbors(example_set, query, k):
    neighbors = []
    for i in query:
        neighbors.append(eDist(example_set,i))
    indices = numpy.argsort(neighbors, axis = 0, kind = 'quicksort')
    return indices[:k]

# Given a n × d example_set matrix where each row represents one example point and a n × 1
# column-vector with these points’ corresponding labels, return the prediction of a kNN classifier for the
# query point. Should use the previous function.
def kNN_classify_point(train_Y, trainingData, k, train_X):
    points = {} 
    for i in range(len(train_Y)):
        neighbors = get_nearest_neighbors(train_Y[i], trainingData, k)
        classify(neighbors, i,train_X,points)
    return points