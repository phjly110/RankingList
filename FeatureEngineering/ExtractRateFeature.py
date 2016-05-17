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

def returnRate(path,date,n_day):

    bookUser_map = {}
    #user_dict = {}
    for i in range(n_day,0,-1):
        day = int(date.split('-')[2]) - i
        print day
        if day < 10:
            date_str = date[:-2] + '0' +str(day)
        else:
            date_str = date[:-2] + str(day)
        f = open(path + date_str)
        line = f.readline()
        while line:
            bookId = line.split(',')[0]
            user_arr = line.split('[')[1].split(']')[0].split(',')
            if bookUser_map.get(bookId):
                user_tempdict = bookUser_map[bookId]
                for user in user_arr:
                    if user_tempdict.get(user):
                        user_tempdict[user] = user_tempdict[user] + 1
                        #bookUser_map[bookId] = user_tempdict
                    else:
                        user_tempdict[user] = 1
                    bookUser_map[bookId] = user_tempdict
            else:
                for user in user_arr:
                    user_tempdict = {}
                    user_tempdict[user] = 1
                bookUser_map[bookId] = user_tempdict
            line = f.readline()

    return bookUser_map

#输出书本被阅读的情况
#example:b0001046,['u026515'	1,]   书籍Id,[用户Id,阅读了几天]
def printBookUser(bookUser_map,date):
    output = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureEngineering/ReturnRate/'+date,'w')
    for key in bookUser_map:
        user_dict = bookUser_map[key]
        output.write(key)
        output.write(',[')
        for user in user_dict:
            output.write(str(user))
            output.write('\t')
            output.write(str(user_dict[user]))
            output.write(',')
        output.write(']')
        output.write('\n')
    return 'printBookUser done...'

#输出了3个特征
#example:b0031962,[56,13,0.23214]   书籍ID,[被阅读人数,n_day内反复阅读人数,返客率]
def printBookUserRate(bookUser_map,date):
    output = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureEngineering/ReturnRate1/'+date,'w')
    for key in bookUser_map:
        user_dict = bookUser_map[key]
        returnNum = 0
        output.write(key)
        output.write(',[')
        output.write(str(len(user_dict)))
        output.write(',')
        for user in user_dict:
            if user_dict[user] != 1:
                returnNum = returnNum + 1
        output.write(str(returnNum))
        output.write(',')
        return_rate = round(float(returnNum)/len(user_dict),5)
        output.write(str(return_rate))
        output.write(']')
        output.write('\n')
    return 'printBookUserRate done...'

def run():
    path = '/Users/phj/Documents/Postgraduate/BookData/BooksPredict/FilterByDay/AllReadSituation/'
    end_date = 31
    n_day = 3      #提取前几天

    for i in range(n_day+1,end_date):
        date = '2013-07-'
        if i < 10:
            date = date + '0' + str(i)
        else:
            date = date + str(i)
        print date
        book_map = returnRate(path,date,n_day)
        out1 = printBookUser(book_map,date)
        print out1
        out2 = printBookUserRate(book_map,date)
        print out2
    return 1

if __name__ == '__main__':
    run()