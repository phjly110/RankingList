# _*_ coding:utf-8 _*_
from os import listdir

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

def loadDate(directions):
    trainFile_lists = []
    for direction in directions:
        trainFile_list = listdir('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureEngineering/'+direction+'/')
        m = len(trainFile_list)
        trainFile_lists.append(trainFile_list[1:])
        #print trainFile_list[1:]
        print m
    print trainFile_lists
    print len(trainFile_lists)
    #找到日期的交集数据
    intersection_list = trainFile_lists[0]
    for i in range(1,len(trainFile_lists)):
        tmp = list(set(intersection_list).intersection(set(trainFile_lists[i])))
        intersection_list = tmp
    intersection_list = sorted(intersection_list)
    print intersection_list
    print directions
    #print directions[0]
    for day in intersection_list:
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
        # for key in bookFeature_map:
        #     print bookFeature_map.get(key)
        output = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureEngineering/Combine/'+day,'w')
        for key in bookFeature_map:
            output.write(key)
            output.write(',')
            output.write('[')
            features_list = bookFeature_map.get(key)
            for i in range(len(features_list)):
                output.write(str(features_list[i]))
                output.write(',')
            #output.write(features_list)
            output.write(']')
            output.write('\n')
        output.close()
    return 1

def run():
    #directions = ['Day1','Day3','Day7','ReturnRate1','OldRate1','ActiveDegree1']
    directions = ['Day1','ReturnRate1','OldRate1','ActiveDegree1']
    loadDate(directions)
    return 1

if __name__ == '__main__':
    run()