import sys, csv, numpy
from knnalgo import * 
from handleCSV import *
trainingFile = "train.csv"
testingFile = "test_pub.csv"
knum = 8
#k values for k-fold
kvals = [1,3,5,7,9,99,999,8000]
#number of folds
num_folds = 4

def combinedSets(firstSet, secondSet, thirdSet):
    return numpy.concatenate((firstSet,secondSet,thirdSet))

#distance function calculates euclidean distance 
def distance(x, xi):
    val = xi[1:-1]
    if flag == 1:
        temp = x[1:-1]
    else:
        temp = x[1:]
    return numpy.linalg.norm(val - temp) 

def load_arr(file):
    data = numpy.genfromtxt(file, dtype = float, delimiter = ',', skip_header=1)
    return data


def calculateAccuracy(train_Y, points):
    sum = 0
    for i in range(len(points)):
        if train_Y[i][-1] == points[i]:
            sum +=1
    return sum/len(points)
    
    
def cross_validation(fulltrain_Y, foldA, foldB, foldC, foldD, train_Y, k):
    subset1 = combinedSets(foldB, foldC, foldD)
    subset2 = combinedSets(foldA, foldC, foldD)
    subset3 = combinedSets(foldA, foldB, foldD)
    subset4 = combinedSets(foldA, foldB, foldC)
    
    pointSet1 = kNN_classify_point(subset1, foldA, k, fulltrain_Y)
    pointSet2 = kNN_classify_point(subset2, foldB, k, fulltrain_Y)
    pointSet3 = kNN_classify_point(subset3, foldC, k, fulltrain_Y)
    pointSet4 = kNN_classify_point(subset4, foldD, k, fulltrain_Y)
    
    accuracyset1 = calculateAccuracy(fulltrain_Y, pointSet1)
    accuracyset2 = calculateAccuracy(fulltrain_Y, pointSet2)
    accuracyset3 = calculateAccuracy(fulltrain_Y, pointSet3)
    accuracyset4 = calculateAccuracy(fulltrain_Y, pointSet4)
    
    var = numpy.var([accuracyset1, accuracyset2, accuracyset3, accuracyset4])
    averageacc = ((accuracyset1 + accuracyset2 + accuracyset3 + accuracyset4)/4) 
    print("when k =", k, accuracyset1, accuracyset2, accuracyset3, accuracyset4, " validation prediction = ", averageacc+space, " variance =", var)
    
        
    
def main():
    train_X = loadCsv(trainingFile)[:,1:]
    train_Y = train_X[:,:-1]

    testingData = loadCsv(testingFile)[:,1:]
    train_Y_Fold = numpy.copy(train_Y)
    foldA = train_Y_Fold[:1999]
    foldB = train_Y_Fold[2000:3999]
    foldC = train_Y_Fold[4000:5999]
    foldD = train_Y_Fold[6000:7999]

    print("Calculating..")
    for k in kvals:
        print("k =", k, "accuracy: ")
        points = kNN_classify_point(train_Y, train_Y, k, train_X)
        accuracy = calculateAccuracy(train_X, points)
        print(accuracy)
    k=1
    points = kNN_classify_point(testingData, train_Y, k, train_X)
    writeCsv(points)
    for k in kvals:
        cross_validation(train_X, foldA, foldB, foldC, foldD, train_Y, k)
    
    for i in range(len(testingData)):
        neighbors = get_nearest_neighbors(testingData[i], train_Y)
        classify(neighbors, i,train_Y,points)
    print(points)

main()