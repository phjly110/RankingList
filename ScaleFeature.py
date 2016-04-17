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
    #对2013/07/07的特征进行归一化,且把阅读量大于20的书籍认为是可能出现在榜单的一个baseline
    data = '2013-07-07_feature18'
    rank_f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/FilterByDay/AllReadSituation/2013-07-08')
    feature_f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureMatrix/'+data)

    baseLine_readCount = 20     #可能进榜单的一个baseline
    feature_len = 18

    rank_line = rank_f.readline()

    book_map = {}      #key为bookId,value是后一天的阅读量值

    while rank_line:
        bookId,read_num = rank_line.split(',')[0],int(rank_line.split(',')[1])
        book_map[bookId] = read_num
        rank_line = rank_f.readline()

    rank_f.close()

    #根据阅读量进行排序,map返回的是list
    book_map = sorted(book_map.iteritems(), key = lambda asd:asd[1], reverse = True )

    #由于排序后map返回的是List,把可能上榜的书籍加入rank_book的set中
    rank_book = set()
    for i in range(0,len(book_map)):
        bookId = book_map[i][0]
        read_num = book_map[i][1]
        if read_num > baseLine_readCount:
            rank_book.add(bookId)
            #print read_num
    #print book_map

    output = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureMatrix/2013-07-07_01','w+')

    feature_line = feature_f.readline()
    max_list = [0]*feature_len          #各个特征的最大值,用作最大-最小归一化
    min_list = [999999]*feature_len     #各个特征的最小值,用作最大-最小归一化
    #得到特征的最大和最小值list
    while feature_line:
        feature_list = feature_line.split('[')[1].split(']')[0].split(',')
        for i in range(0,len(feature_list)):
            feature_list[i] = float(feature_list[i])
            if feature_list[i] > max_list[i]:
                max_list[i] = feature_list[i]
            if feature_list[i] < min_list[i]:
                min_list[i] = feature_list[i]
        feature_line = feature_f.readline()
    print max_list
    print min_list

    feature_f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureMatrix/'+data)
    feature_line = feature_f.readline()

    #对所有特征进行最大-最小归一化
    #加上分类的标签(0-1)是否会出现在榜单上
    while feature_line:
        bookId = feature_line.split(',')[0]
        feature_list = feature_line.split('[')[1].split(']')[0].split(',')
        for i in range(0,len(feature_list)):
            feature_list[i] = float(feature_list[i])
            scale_rate = round((feature_list[i]-min_list[i])/(max_list[i]-min_list[i]), 5)
            output.write(str(scale_rate))
            if i != len(feature_list)-1:
                output.write(',')
        #加上分类标签
        if bookId in rank_book:
            output.write('\t'+'1')
        else:
            output.write('\t'+'0')
        output.write('\n')
        feature_line = feature_f.readline()

    feature_f.close()
    output.close()

if __name__ == '__main__':
    run()