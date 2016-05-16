# _*_ coding:utf-8 _*_

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

def returnRate():
    return 1

def run():
    path = '/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/SplitByDay/'
    end_date = 31
    n_day = 7      #提取前几天
    for i in range(n_day+1,end_date):
        date = '2013-07-'
        if i < 10:
            date = date + '0' + str(i)
        else:
            date = date + str(i)
        print date

    return 1

if __name__ == '__main__':
    run()