# _*_ coding = utf-8 _*_
import numpy as np
import scipy

def generateLabel(X):
    Y = []
    #function y = 1*x1+2*x2+3*x3+4*x4+5*x5+6
    theta = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    for i in X:
        Y.append(scipy.dot(theta,i)+np.random.uniform(0,0.5))
    return Y

def run():
    f = open('Data/13_features.txt' , 'w')
    #f.readline()
    # generate feature matrix X
    X = [[i,i+np.random.randint(1,5),i+np.random.randint(1,5),i+np.random.randint(1,5),i+np.random.randint(1,5)
            ,i+np.random.randint(1,5),i+np.random.randint(1,5),i+np.random.randint(1,5),i+np.random.randint(1,5)
            ,i+np.random.randint(1,5),i+np.random.randint(1,5),i+np.random.randint(1,5),i+np.random.randint(1,5),1]
         for i in range(0, 200)]

    #print X
    print len(X[1])
    Y = generateLabel(X)
    #print Y

    #print len(Y)
    for i in range(0,len(X)):
        #print X[i]
        for j in range(0,len(X[i])):
            #print X[i][j]
            f.write(str(X[i][j]))
            if j < len(X[i])-1:
                f.write(',')
        f.write('\t')
        f.write(str(Y[i]))
        f.write('\n')
    f.close()

if __name__ == '__main__':
    run()