#  _*_ coding:utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt

class BookCondition:
    bookId = ''
    eventId = 0
    num = 0
    user_Set = set()
    def __init__(self,bookId,eventId,num,user_Set):
        self.bookId = bookId
        self.eventId = eventId
        self.num = num
        self.user_Set = user_Set
    def printAll(self):
        return ("%s, %s, %s, %s" %(self.bookId, self.eventId, self.num, list(self.user_Set)))

def searchInClickCatalog(search_date, search_bookId):
    f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/ClickCatalog')

    line = f.readline()

    dayMap = {}


    while line:
        userId,bookId,eventId,time = line.split(',')
        date = time.split(' ')[0]
        day = int(date.split('/')[2])
        if bookId == search_bookId and int(search_date.split('/')[2])-8 < day < int(search_date.split('/')[2])+1:
            if dayMap.get(date):
                user_set = dayMap.get(date)
                user_set.add(userId)
                dayMap[date] = user_set
            else:
                user_set = set()
                user_set.add(userId)
                dayMap[date] = user_set
        line = f.readline()
    f.close()
    print eventId
    return dayMap

def searchInDwelltime(search_date, search_bookId):
    f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/dwelltime')

    line = f.readline()
    dayMap = {}

    while line:
        userId,bookId,time = line.split(',')
        eventId = 5
        date = time.split('\t')[0]
        day = int(date.split('/')[2])
        if bookId == search_bookId and int(search_date.split('/')[2])-8 < day < int(search_date.split('/')[2])+1:
            if dayMap.get(date):
                user_set = dayMap.get(date)
                user_set.add(userId)
                dayMap[date] = user_set
            else:
                user_set = set()
                user_set.add(userId)
                dayMap[date] = user_set
        line = f.readline()
    f.close()
    print eventId
    return dayMap

def searchInClickCover(search_date, search_bookId):
    f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/ClickCover')

    line = f.readline()

    dayMap = {}


    while line:
        userId,bookId,eventId,time = line.split(',')
        date = time.split(' ')[0]
        day = int(date.split('/')[2])
        if bookId == search_bookId and int(search_date.split('/')[2])-8 < day < int(search_date.split('/')[2])+1:
            if dayMap.get(date):
                user_set = dayMap.get(date)
                user_set.add(userId)
                dayMap[date] = user_set
            else:
                user_set = set()
                user_set.add(userId)
                dayMap[date] = user_set
        line = f.readline()

    f.close()
    print eventId
    return dayMap

def searchInDownload(search_date, search_bookId):
    f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/Download')

    line = f.readline()

    dayMap = {}


    while line:
        userId,bookId,eventId,time = line.split(',')
        date = time.split(' ')[0]
        day = int(date.split('/')[2])
        if bookId == search_bookId and int(search_date.split('/')[2])-8 < day < int(search_date.split('/')[2])+1:
            if dayMap.get(date):
                user_set = dayMap.get(date)
                user_set.add(userId)
                dayMap[date] = user_set
            else:
                user_set = set()
                user_set.add(userId)
                dayMap[date] = user_set
        line = f.readline()

    f.close()
    print eventId
    return dayMap

def searchInDelsub(search_date, search_bookId):
    f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/Delsub')

    line = f.readline()

    dayMap = {}


    while line:
        userId,bookId,eventId,time = line.split(',')
        date = time.split(' ')[0]
        day = int(date.split('/')[2])
        if bookId == search_bookId and int(search_date.split('/')[2])-8 < day < int(search_date.split('/')[2])+1:
            if dayMap.get(date):
                user_set = dayMap.get(date)
                user_set.add(userId)
                dayMap[date] = user_set
            else:
                user_set = set()
                user_set.add(userId)
                dayMap[date] = user_set
        line = f.readline()

    f.close()
    print eventId
    return dayMap


def searchInAddsub(search_date, search_bookId):
    f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/Addsub')

    line = f.readline()

    dayMap = {}


    while line:
        userId,bookId,eventId,time = line.split(',')
        date = time.split(' ')[0]
        day = int(date.split('/')[2])
        #print date
        if bookId == search_bookId and int(search_date.split('/')[2])-8 < day < int(search_date.split('/')[2])+1:
            if dayMap.get(date):
                user_set = dayMap.get(date)
                user_set.add(userId)
                dayMap[date] = user_set
            else:
                user_set = set()
                user_set.add(userId)
                dayMap[date] = user_set
        line = f.readline()
    f.close()
    print eventId
    # print len(user_set)
    # print user_set
    return dayMap

def run():
    date = '2013/07/25'  #输入要搜索的日期
    bookId = 'b0003278'   #输入要搜索的书籍
    map_arr = []
    dayMap1 = searchInAddsub(date,bookId)
    dayMap2 = searchInDelsub(date,bookId)
    dayMap3 = searchInDownload(date,bookId)
    dayMap4 = searchInClickCover(date,bookId)
    dayMap5 = searchInDwelltime(date,bookId)
    dayMap6 = searchInClickCatalog(date,bookId)

    map_arr.append(dayMap1)
    map_arr.append(dayMap2)
    map_arr.append(dayMap3)
    map_arr.append(dayMap4)
    map_arr.append(dayMap5)
    map_arr.append(dayMap6)

    #dayMap = sorted(dayMap.iteritems(), key = lambda asd:asd[0],reverse = False)
    color_arr = ['b','c','g','k','m','r','y','b','c','g']
    n = 8
    X = np.arange(n) + 1
    count_Num = 0
    for dayMap in map_arr:
        addSub_arr = []
        for key in dayMap:
            addSub_arr.append([int(date.split('/')[2])-int(key.split('/')[2]),len(dayMap.get(key))])
        addSub_arr = sorted(addSub_arr,reverse=True)

        Y = [addSub_arr[i][1] for i in range(0,len(addSub_arr))]
        plt.bar(X+0.15*count_Num,Y,width=0.15,facecolor=color_arr[count_Num],edgecolor='white')
        count_Num = count_Num + 1
        print addSub_arr

    plt.show()
if __name__ == '__main__':
    run()
    #a = [[1,2],[3,4],[5,6],[7,8],[9,0]]
    #b = [a[i][1] for i in range(0,len(a))]
    #print b