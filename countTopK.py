# _*_ coding:utf-8 _*_

class EachDay:
    bookId = ''    #书籍ID
    userNum = 0    #书被多少用户阅读
    user_Set = set()    #阅读该书籍的集合
    def __init__(self,book,num,user):
        self.bookId = book
        self.userNum = num
        self.user_Set = user
    def printAll(self):
        return ("%s, %s, %s" %(self.bookId, self.userNum, list(self.user_Set)))
    def getBookId(self):
        return self.bookId
    def getUserNum(self):
        return self.userNum
    def getUserSet(self):
        return self.user_Set

class ReadSituation:
    bookId = ''
    readNum_arr = []
    def __init__(self,bookId,readNum_arr):
        self.bookId = bookId
        self.readNum_arr = readNum_arr
    def printAll(self):
        return ("%s, %s" %(self.bookId, self.readNum_arr))


if __name__ == "__main__":

    allReadSituationOutput = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/FilterByDay/AllReadSituation/allReadSituation','w')
    yearAndMonth = "2013/07/"

    for i in range(0,30):
        f = open("/Users/phj/Documents/Postgraduate/BookData/BooksPredict/dwelltime")
        i = i+1
        book_map = {}
        line = f.readline()
        if i < 10:
            date = yearAndMonth + "0" + str(i)
        else:
            date = yearAndMonth + str(i)

        #使输出时文件为2013-07-**
        print date.replace('/','-')

        while line:
            user,book,time = line.split(",")
            if time.split("\t")[0] == date:
                if book_map.get(book):
                    user_set = book_map.get(book)
                    user_set.add(user)
                    book_map[book] = user_set
                else:
                    user_set = set()
                    user_set.add(user)
                    book_map[book] = user_set
            line = f.readline()

        f.close()
        eachDay_arr = []      #存放一整天的书籍阅读情况list,元素对象为EachDay

        #为每一本书建立EachDay的对象,并加入到eachDay_arr的list中
        for key in book_map:
            user_set = book_map.get(key)
            eachDay = EachDay(key,len(user_set),user_set)
            eachDay_arr.append(eachDay)

        #根据书籍每天的阅读量进行排序
        eachDay_arr = sorted(eachDay_arr,key = lambda asd:asd.userNum,reverse=True)

        #为生成ReadSituation的对象,把每天阅读量情况进行统计(用户名不统计)
        readNum_arr = []
        for i in eachDay_arr:
            readNum_arr.append(i.getUserNum())
        oneReadSituation = ReadSituation(date.replace('/','-'),readNum_arr)
        allReadSituationOutput.write(oneReadSituation.printAll())
        allReadSituationOutput.write('\n')

        #按每天一个文件进行输出
        # output = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/FilterByDay/AllReadSituation/'+date.replace('/','-'),'w')
        # for i in eachDay_arr:
        #     if i.getUserNum() > 0:
        #         output.write(i.printAll())
        #         output.write('\n')
        #
        # output.close()

    allReadSituationOutput.close()