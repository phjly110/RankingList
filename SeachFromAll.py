#  _*_ coding:utf-8 _*_

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

    user_set = set()

    while line:
        userId,bookId,eventId,time = line.split(',')
        date = time.split(' ')[0]
        #print date
        if bookId == search_bookId and date == search_date:
            user_set.add(userId)
        line = f.readline()
    print eventId
    print len(user_set)
    print user_set

def searchInDwelltime(search_date, search_bookId):
    f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/dwelltime')

    line = f.readline()

    user_set = set()

    while line:
        userId,bookId,time = line.split(',')
        eventId = 5
        date = time.split('\t')[0]
        #print date
        if bookId == search_bookId and date == search_date:
            user_set.add(userId)
        line = f.readline()
    print eventId
    print len(user_set)
    print user_set

def searchInClickCover(search_date, search_bookId):
    f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/ClickCover')

    line = f.readline()

    user_set = set()

    while line:
        userId,bookId,eventId,time = line.split(',')
        date = time.split(' ')[0]
        #print date
        if bookId == search_bookId and date == search_date:
            user_set.add(userId)
        line = f.readline()
    print eventId
    print len(user_set)
    print user_set

def searchInDownload(search_date, search_bookId):
    f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/Download')

    line = f.readline()

    user_set = set()

    while line:
        userId,bookId,eventId,time = line.split(',')
        date = time.split(' ')[0]
        #print date
        if bookId == search_bookId and date == search_date:
            user_set.add(userId)
        line = f.readline()
    print eventId
    print len(user_set)
    print user_set

def searchInDelsub(search_date, search_bookId):
    f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/Delsub')

    line = f.readline()

    user_set = set()

    while line:
        userId,bookId,eventId,time = line.split(',')
        date = time.split(' ')[0]
        #print date
        if bookId == search_bookId and date == search_date:
            user_set.add(userId)
        line = f.readline()
    print eventId
    print len(user_set)
    print user_set


def searchInAddsub(search_date, search_bookId):
    f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/Addsub')

    line = f.readline()

    user_set = set()

    while line:
        userId,bookId,eventId,time = line.split(',')
        date = time.split(' ')[0]
        #print date
        if bookId == search_bookId and date == search_date:
            user_set.add(userId)
        line = f.readline()

    print eventId
    print len(user_set)
    print user_set


def run():
    date = '2013/07/24'
    bookId = 'b0003278'
    searchInAddsub(date,bookId)
    searchInDelsub(date,bookId)
    searchInDownload(date,bookId)
    searchInClickCover(date,bookId)
    searchInDwelltime(date,bookId)
    searchInClickCatalog(date,bookId)

if __name__ == '__main__':
    run()