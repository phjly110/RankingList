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

def run():
    data = '2013-07-07_feature18'
    rank_f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/FilterByDay/AllReadSituation/2013-07-08')
    feature_f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureMatrix/'+data)

    rank_line = rank_f.readline()

    book_map = {}

    while rank_line:
        bookId,read_num = rank_line.split(',')[0],int(rank_line.split(',')[1])
        book_map[bookId] = read_num
        rank_line = rank_f.readline()

    rank_f.close()

    book_map = sorted(book_map.iteritems(), key = lambda asd:asd[1], reverse = True )

    rank_book = set()
    for i in range(0,len(book_map)):
        bookId = book_map[i][0]
        read_num = book_map[i][1]
        if read_num > 20:
            rank_book.add(bookId)
            #print read_num
    #print book_map

    output = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureMatrix/2013-07-07_01','w+')

    feature_line = feature_f.readline()

    max_list = [0]*18

    while feature_line:
        bookId = feature_line.split(',')[0]

        feature_list = feature_line.split('[')[1].split(']')[0].split(',')
        for i in range(0,len(feature_list)):
            feature_list[i] = float(feature_list[i])
            output.write(str(feature_list[i]))
            if i != len(feature_list)-1:
                output.write(',')

        if bookId in rank_book:
            print bookId
            output.write('\t'+'1')
        else:
            output.write('\t'+'0')

        output.write('\n')
        feature_line = feature_f.readline()

    feature_f.close()
    output.close()

if __name__ == '__main__':
    run()