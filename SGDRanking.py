# _*_ coding = utf-8 _*_

from numpy import *
import scipy

def readData(dataPath):
    points = genfromtxt("/Data/data.csv", delimiter=",")
def run():
    x,y = readData()


if __name__ == '__main__':
    run()