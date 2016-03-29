# _*_ coding:utf-8 _*_

def run(self):

    yearAndMonth = '2013/07/'

    for i in range(0,30):
        f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/Addsub')
        i = i+1
        if  i < 10:
            date = yearAndMonth +'0'+str(i)
        else:
            date = yearAndMonth + str(i)
        line = f.readline()
        while line:
            userId,bookId,eventID,timeStamp = line.split(',')
            date_timeStamp = timeStamp.split('\t')[0]
            line = f.readline()
        f.close()

if __name__ == "__main__":
    run()