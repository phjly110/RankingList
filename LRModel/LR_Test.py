# _*_ coding:utf-8 _*_
import math
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

def run():
    min_max_scaler = preprocessing.MinMaxScaler(feature_range=(-1,1))
    df = pd.read_csv('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureEngineering/Combine_csv/2013-07-09.csv')

    #clean the data
    df.columns = ['bookID','label','fea0','fea1','fea2','fea3','fea4','fea5','fea6','fea7','fea8','fea9','fea10','fea11','fea12','fea13',
                  'fea14','fea15','fea16','fea17','fea18','fea19','fea20','fea21','fea22','fea23','fea24','fea25','fea26']
    x = df['label'].map(lambda x: float(x))

    X = df[['fea0','fea1','fea2','fea3','fea4','fea5','fea6','fea7','fea8','fea9','fea10','fea11','fea12','fea13','fea14','fea15','fea16','fea17','fea18','fea19','fea20','fea21','fea22','fea23','fea24','fea25','fea26']]
    X = np.array(X)
    X = min_max_scaler.fit_transform(X)
    Y = df['label'].map(lambda x: float(x))
    Y = np.array(Y)

    #creating training and testing dataset
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.33)

    #train scikit learn model
    clf = LogisticRegression()
    clf.fit(X_train,Y_train)
    print clf.get_params()
    print 'score Scikit learn:', clf.score(X_test,Y_test)

#-----------------------------------------------

    def Sigmod(z):
        G_of_Z = float(1.0 / float(1.0 + math.exp(-1.0*z)))
        return G_of_Z

    def Hypothesis(theta,x):
        z = 0
        for i in xrange(len(theta)):
            z += x[i]*theta[i]
        return Sigmod(z)

    def Cost_Function(X,Y,theta,m):
        sumOfErrors = 0
        for i in xrange(m):
            xi = X[i]
            hi = Hypothesis(theta,xi)
            if Y[i] == 1:
                error = Y[i] * math.log(hi)
            elif Y[i] == 0:
                error = (1-Y[i]) * math.log(1-hi)
            sumOfErrors += error
        const = -1/m
        J = const * sumOfErrors
        print 'cost is ', J
        return J

    def Cost_Function_Derivative(X,Y,theta,j,m,alpha):
        sumErrors = 0
        for i in xrange(m):
            xi = X[i]
            xij = xi[j]
            hi = Hypothesis(theta,X[i])
            error = (hi - Y[i])*xij
            sumErrors += error
        m = len(Y)
        constant = float(alpha)/float(m)
        J = constant * sumErrors
        return J

    def Gradient_Descent(X,Y,theta,m,alpha):
        new_theta = []
        constant = alpha/m
        for j in xrange(len(theta)):
            CFDerivative = Cost_Function_Derivative(X,Y,theta,j,m,alpha)
            new_theta_value = theta[j] -CFDerivative
            new_theta.append(new_theta_value)
        return new_theta

    def Declare_Winner(theta):
        score = 0
        winner = ''
        scikit_score = clf.score(X_test,Y_test)
        length = len(X_test)
        for i in xrange(length):
            prediction = round(Hypothesis(X_test[i],theta))
            answer = Y_test[i]
            if prediction == answer:
                score += 1
        my_score = float(score) / float(length)
        if my_score > scikit_score:
            print 'You won!'
        elif my_score == scikit_score:
            print 'Its a tie!'
        else:
            print 'scikit won...'
        print 'Your score: ', my_score
        print 'Scikits score: ', scikit_score

    def Logistic_Regression(X,Y,alpha,theta,num_iters):
        m = len(Y)
        for x in xrange(num_iters):
            new_theta = Gradient_Descent(X,Y,theta,m,alpha)
            theta = new_theta
            if x % 100 == 0:
                Cost_Function(X,Y,theta,m)
                print 'theta ',theta
                print 'cost is ', Cost_Function(X,Y,theta,m)
        Declare_Winner(theta)

    #setting variables
    initial_theta = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    alpha = 0.1
    iterations = 1000
    #Logistic_Regression(X,Y,alpha,initial_theta,iterations)


    return 1

if __name__ == '__main__':
    run()