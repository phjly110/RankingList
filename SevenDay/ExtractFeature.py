# _*_ coding:utf-8 _*_

def extractFeature(date,preDay):
    bookMap = {}
    for i in range(preDay):
        day = int(date.split('-')[2]) - 1
        if day < 10:
            date = date[0:len(date)-2] + '0' + str(day)
        else:
            date = date[0:len(date)-2] + str(day)
        print date

        f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/FilterByDay/AllReadSituation/' + date)
        line = f.readline()
        while line:
            bookId = line.split(',')[0]
            readCount = line.split(',')[1]
            if bookMap.get(bookId):
                readArr = bookMap[bookId]
                readArr[preDay-1-i] = int(readCount)
                bookMap[bookId] = readArr
            else:
                readArr = [0]*7
                readArr[preDay-1-i] = int(readCount)
                bookMap[bookId] = readArr
            line = f.readline()
    return bookMap

def run():
    date = '2013-07-09'
    preDay = 7
    bookMap = extractFeature(date,preDay)

    output = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/SevenDay/'+date,'w')

    for key in bookMap:
        output.write(key)
        output.write('\t')
        output.write(str(bookMap[key]))
        output.write('\n')
        #print bookMap[key]
    return 1

if __name__ == '__main__':
    run()