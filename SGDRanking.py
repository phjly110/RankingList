# _*_ coding = utf-8 _*_

from numpy import *
import scipy

def step_gradient(features_X, label_y, theta, learning_rate):
    new_theta = theta
    sum_D_value = [0]*14
    # i means the number of samples
    for i in range(0,len(theta)):
        sum_D_value = map(lambda (a,b):a+b, zip(sum_D_value,(label_y[i] - scipy.dot(new_theta,features_X[i])) * features_X[i]))
        #sum_D_value += (label_y[i] - scipy.dot(new_theta,features_X[i])) * features_X[i]
        print sum_D_value
    #print sum_D_value
    new_theta = new_theta + learning_rate * sum_D_value
    return new_theta

def GDRegression(features_X, label_y, learning_rate, initial_theta, num_iterations):
    final_theta = initial_theta
    for i in range(0,num_iterations):
        final_theta = step_gradient(features_X, label_y,final_theta,learning_rate)
    return final_theta

def readData(dataPath):
    f = open(dataPath)
    X = []
    y = []
    line = f.readline()
    while line:
        features = list(map(float,line.split('\t')[0].split(',')))
        label = float(line.split('\t')[1].strip())
        X.append(features)
        y.append(label)
        line = f.readline()
    return X,y

def run():
    X,y = readData('Data/13_features.txt')
    #print X[1]
    #print y[1]
    learning_rate = 0.1
    initial_theta = [0]*len(X[1])
    #print initial_theta
    num_iterations = 1000
    theta = GDRegression(X,y,learning_rate,initial_theta,num_iterations)
    print theta


if __name__ == '__main__':
    run()