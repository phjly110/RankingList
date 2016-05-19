# _*_ coding:utf-8 _*_
from os import listdir

def loadDate(directions):
    
    for direction in directions:
        trainFile_list = listdir('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureEngineering/'+direction+'/')
        m = len(trainFile_list)
        for trainFile in trainFile_list[1:]:
            f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureEngineering/'+direction+'/'+trainFile)
            line = f.readline()
            while line:

                line = f.readline()
            f.close()
        print trainFile_list[1:]
        print m

    return 1

def run():
    directions = ['Day1','Day3','Day7','ReturnRate1','OldRate1','ActiveDegree1']
    loadDate(directions)
    return 1

if __name__ == '__main__':
    run()