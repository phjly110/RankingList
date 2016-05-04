# _*_ coding:utf-8 _*_
import scipy
import math

def sigmod(inX, inTheta):
    t = scipy.dot(inTheta,inX)
    return 1.0/(1 + math.exp(-t))

def readData(dataPath):
    f = open(dataPath)
    X = []
    Y = []
    line = f.readline()
    while line:
        features = list(map(float,line.split('\t')[0].split('[')[1].split(']')[0].split(',')))
        label_y = int(line.split('\t')[1].strip())

        X.append(features)
        Y.append(label_y)
        line = f.readline()
    return X,Y

def run():
    X,Y = readData('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/SevenDay/2013-07-08_train')
    theta = [0.5574013854970027, 0.16953616793611667, -0.13477894841198645, -0.3927773601132772, 0.016317156111841456, -0.3756946754623091, -0.22189286230837388]
    for i in range(len(X)):
        h = sigmod(X[i],theta)
        if h > 0.75:
            #if int(Y[i]) != 1:
            print i
        # else:
        #     if int(Y[i]) != 0:
        #         print i
if __name__ == '__main__':
    run()