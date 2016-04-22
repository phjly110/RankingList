# _*_ coding:utf-8 _*_

def testFeatureLen(path,featureLen):
    f = open(path)
    line = f.readline()

    while line:
        features_list = line.split('[')[1].split(']')[0].split(',')
        if len(features_list) != featureLen:
            print len(features_list)
            print line
        line = f.readline()
    f.close()

def searchBook(date,mergeDay,searchBookId):

    for j in range(mergeDay):
        day = int(date.split('-')[2])-j
        if day < 10:
            date_str = date[:-2] + "0" + str(day)
        else:
            date_str = date[:-2] + str(day)
        print date_str

        f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureMatrix/'+date_str+'_feature18')
        line = f.readline()
        while line:
            bookId = line.split(',')[0]
            #print bookId
            if bookId == searchBookId:
                print line
            line = f.readline()

        f.close()

def run():
    # date = '2013-07-07'
    # mergeDay = 7
    # bookId = 'b0026235'
    # searchBook(date,mergeDay,bookId)

    path = '/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/feature_3Merge/2013-07-07_feature'
    testFeatureLen(path,54)


if __name__ == '__main__':
    run()