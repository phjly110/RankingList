# _*_ coding:utf-8 _*_
from os import listdir
import scipy
import math
import time

class bookFeature:
    bookId = ''
    feature_arr = []

    def __init__(self,bookId,feature_arr):
        self.bookId = bookId
        self.feature_arr = feature_arr

    def printAll(self):
        return ("%s,%s" %(self.bookId,list(self.feature_arr)))

    def getFeatureArr(self):
        return ("%s" %(list(self.feature_arr)))

    def getBookId(self):
        return ("%s" %(self.bookId))

def sigmod(inX,inTheta):
    t = scipy.dot(inTheta,inX)
    return 1.0/(1+math.exp(-t))

#生成合并数据,为了特征组合用的函数
def generateCombineData(directions):
    trainFile_lists = []
    for direction in directions:
        trainFile_list = listdir('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureEngineering/'+direction+'/')
        m = len(trainFile_list)
        trainFile_lists.append(trainFile_list[1:])
        #print trainFile_list[1:]
        #print m
    print trainFile_lists
    #print len(trainFile_lists)
    #找到日期的交集数据
    intersection_list = trainFile_lists[0]
    for i in range(1,len(trainFile_lists)):
        tmp = list(set(intersection_list).intersection(set(trainFile_lists[i])))
        intersection_list = tmp
    intersection_list = sorted(intersection_list)
    print intersection_list
    print directions
    print 'data generating...'
    for day in intersection_list:
        print day
        bookFeature_map = {}
        featureNum = 0
        for direction in directions:
            f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureEngineering/'+direction+'/'+day)
            line = f.readline()
            featureNumTmp = 0
            while line:
                bookId = line.split(',')[0]
                feature_list = line.split('[')[1].split(']')[0].split(',')
                featureNumTmp = len(feature_list)
                if bookFeature_map.get(bookId):
                    features_arr = bookFeature_map.get(bookId)
                    for i in range(len(feature_list)):
                        features_arr.append(feature_list[i])
                        bookFeature_map[bookId] = features_arr
                else:
                    features_list = []
                    for i in range(featureNum):
                        features_list.append(0)
                    features_list.extend(feature_list)
                    bookFeature_map[bookId] = features_list
                #bookFeature(bookId,features_list)
                line = f.readline()
            featureNum = featureNum + featureNumTmp
        f.close()
        #对于feature中长度不足的特征向量进行"0"补全
        for key in bookFeature_map:
            tmp_list = bookFeature_map.get(key)
            for i in range(len(tmp_list),featureNum):
                tmp_list.append(0)
            bookFeature_map[key] = tmp_list

        #找出可能入榜单的书籍
        bookRank_f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/FilterByDay/AllReadSituation/'+day)
        bookRank_map = {}
        line = bookRank_f.readline()
        while line:
            bookId,readNum = line.split(',')[0],int(line.split(',')[1])
            if readNum > 20:
                bookRank_map[bookId] = 1
            line = bookRank_f.readline()
        bookRank_f.close()

        #将特征输出,方便数据的观察
        output = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureEngineering/Combine1/'+day,'w')
        for key in bookFeature_map:
            output.write(key)
            output.write(',')
            if bookRank_map.get(key):
                output.write(str(1))
            else:
                output.write(str(0))
            output.write(',')
            output.write('[')
            features_list = bookFeature_map.get(key)
            for i in range(len(features_list)-1):
                output.write(str(features_list[i]))
                output.write(',')
            output.write(str(features_list[len(features_list)-1]))
            output.write(']')
            output.write('\n')
        output.close()
    return 'generate data is OK...'

#读取训练数据
def loadData(path):
    print 'loading data...'
    dataArray = []
    labelArray = []
    trainFile_list = listdir(path)
    trainFile_list = trainFile_list[1:]
    trainFile_list = sorted(trainFile_list)
    for day in trainFile_list:
        print day
        f = open(path + day)
        dataDayArray = []
        labelDayArray = []
        line = f.readline()
        while line:
            featureArray = []
            label = line.split(',')[1]
            feature_list = line.split('[')[1].split(']')[0].split(',')
            labelDayArray.append(int(label))
            for i in range(len(feature_list)):
                featureArray.append(float(feature_list[i]))
            dataDayArray.append(featureArray)
            line = f.readline()
        dataArray.append(dataDayArray)
        labelArray.append(labelDayArray)
    #print trainFile_list
    return dataArray,labelArray

def run():
    #directions = ['Day1','Day3','Day7','ReturnRate1','OldRate1','ActiveDegree1']
    directions = ['Day1','ReturnRate1','OldRate1','ActiveDegree1']
    #生成组合数据
    #outlet_str = generateCombineData(directions)
    #print outlet_str

    dataArray,labelArray = loadData('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureEngineering/Combine1/')
    print 'loadData is Done...'
    print len(dataArray)
    print len(labelArray)
    # for i in range(len(dataArray)):
    #     for j in range(20):
    print dataArray[10][10]
    print labelArray[10][10]
    return 1

if __name__ == '__main__':
    run()