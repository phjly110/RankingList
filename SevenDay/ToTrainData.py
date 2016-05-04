# _*_ coding:utf-8 _*_

def run():
    date = '2013-07-08'
    f1 = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/FilterByDay/AllReadSituation/'+ date)
    line = f1.readline()
    bookSet = set()
    while line:
        bookId,readCount = line.split(',')[0],int(line.split(',')[1])
        if readCount > 20:
            bookSet.add(bookId)
        line = f1.readline()
    f1.close()
    f2 = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/SevenDay/'+date)
    output = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/SevenDay/'+date+'_train','w')
    line = f2.readline()
    while line:
        bookId,featureArr = line.split('\t')[0],line.split('\t')[1].strip()
        output.write(featureArr)
        output.write('\t')
        if bookId in bookSet:
            output.write('1')
        else:
            output.write('0')
        output.write('\n')
        line = f2.readline()
    f2.close()
    output.close()

    return 1

if __name__ == '__main__':
    run()