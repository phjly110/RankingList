# _*_ coding:utf-8 _*_
import scipy
import math


def sigmod(inX, inTheta):
    t = scipy.dot(inTheta,inX)
    return 1.0/(1 + math.exp(-t))

def GDLogisticRegression(features_X, label_Y, learning_rate, initial_theta, num_iterations):
    loss = 50
    iters = 1
    Eps = 0.0001
    while loss > Eps and iters < num_iterations:
        loss = 0
        for i in range(len(features_X)):
            h = sigmod(features_X[i],initial_theta)
            for j in range(len(initial_theta)):
                initial_theta[j] = initial_theta[j] + learning_rate*(label_Y[i]-h)*features_X[i][j]
            #print initial_theta
        for i in range(len(features_X)):
            Error = 0
            h = sigmod(initial_theta, features_X[i])
            Error = h -label_Y[i]
            Error = Error*Error
            loss = loss + Error
        iters = iters + 1
        print iters
    print 'iters=',iters
    return initial_theta


def readData(dataPath):
    f = open(dataPath)
    X = []
    Y = []
    line = f.readline()
    while line:
        features = list(map(float,line.split('\t')[0].split(',')))
        label_y = int(line.split('\t')[1].strip())

        X.append(features)
        Y.append(label_y)
        line = f.readline()
    return X,Y

def run():
    X,Y = readData('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureMatrix/2013-07-07_01')

    learning_rate = 0.01
    initial_theta = [0]*len(X[0])
    num_iterations = 5000
    theta = GDLogisticRegression(X,Y,learning_rate,initial_theta,num_iterations)
    print theta

if __name__ == '__main__':
    run()