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
        features = list(map(float,line.split('\t')[0].split(',')))
        label_y = int(line.split('\t')[1].strip())

        X.append(features)
        Y.append(label_y)
        line = f.readline()
    return X,Y

def run():
    X,Y = readData('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureMatrix/2013-07-07_01')
    theta = [63.39789923183883, 60.95497701680332, -22.47465983845871, -26.195212881027057, -5.922811085219206, -165.99418821789536, 24.19578503428875, 12.575239868245912, 23.206069192961444, 15.82493984462311, 49.89005956141158, 114.15024304626647, 55.94756430817859, -109.89774578597023, -62.162959975884064, 7.885104316385161, -14.84400319820061, -29.518190036989015]

    for i in range(len(X)):
        h = sigmod(X[i],theta)
        if h > 0.50:
            print i

if __name__ == '__main__':
    run()