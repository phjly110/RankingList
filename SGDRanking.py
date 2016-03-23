# _*_ coding = utf-8 _*_

from numpy import *
import scipy

def step_gradient(features_X, label_y, theta, learning_rate):
    new_theta = theta
    sum_D_value = [0]*14
    # i means the number of samples
    for i in range(0,len(theta)):
        #if i == 0:
        extremun = [(label_y[i] - scipy.dot(new_theta,features_X[i])) * x for x in features_X[i]] #* features_X[i]
        print extremun
        print features_X[i]
        sum_D_value = map(lambda (a,b):a+b, zip(sum_D_value,extremun))
        print sum_D_value
        #sum_D_value += (label_y[i] - scipy.dot(new_theta,features_X[i])) * features_X[i]
        #print sum_D_value
    #print sum_D_value
    rate_extrmun = [learning_rate * x for x in sum_D_value]
    print rate_extrmun
    new_theta = map(lambda (a,b):a+b, zip(new_theta, rate_extrmun))
    return new_theta

def GDRegression(features_X, label_y, learning_rate, initial_theta, num_iterations):
    # final_theta = initial_theta
    # for i in range(0,num_iterations):
    #     final_theta = step_gradient(features_X, label_y,final_theta,learning_rate)
    # return final_theta
    loss = 50
    iters = 1
    Eps = 0.0001
    while loss>Eps and iters <num_iterations :
        loss = 0
        for i in range(len(features_X)) :
            h = scipy.dot(initial_theta, features_X[i])
            #h = theta[0]*matrix_A[i][0] + theta[1]*matrix_A[i][1]
            for j in range(len(initial_theta)):
                initial_theta[j] = initial_theta[j] + learning_rate*(label_y[i]-h)*features_X[i][j]

                #theta[1] = theta[1] + leraing_rate*(Matrix_y[i]-h)*matrix_A[i][1]
            print initial_theta
        for i in range(len(features_X)) :
            Error = 0
            h = scipy.dot(initial_theta, features_X[i])
            Error = h - label_y[i]
            Error = Error*Error
            loss = loss +Error
        iters = iters +1
    print 'iters=',iters
    return initial_theta

def readData(dataPath):
    f = open(dataPath)
    X = []
    y = []
    line = f.readline()
    while line:
        features = list(map(float,line.split('\t')[0].split(',')))
        label = float(line.split('\t')[1].strip())
        #features = list(map(float,line.split(',')[0].split(',')))
        #label = float(line.split(',')[1].strip())
        X.append(features)
        y.append(label)
        line = f.readline()
    return X,y

def run():
    #X,y = readData('../MLTest/data.csv')
    #X,y = readData('Data/13_features.txt')
    X,y = readData('Data/test_data.txt')
    print X[1]
    print y[1]
    learning_rate = 0.01
    initial_theta = [0]*len(X[1])
    #print initial_theta
    num_iterations = 5000
    theta = GDRegression(X,y,learning_rate,initial_theta,num_iterations)
    print theta


if __name__ == '__main__':
    run()