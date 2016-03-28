# _*_ coding:utf-8 _*_

class EachDay:
    bookId = ''
    userNum = 0
    user_Set = set()
    def __init__(self,book,num,user):
        self.bookId = book
        self.userNum = num
        self.user_Set = user
    def printAll(self):
        return ("%s, %s, %s" %(self.bookId, self.userNum, list(self.user_Set)))
    def getBookId(self):
        return self.bookId

if __name__ == "__main__":

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

        print date
        print date.replace('/','-')
        #for i in range(0,30):

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

        output = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/FilterByDay/'+date.replace('/','-'),'w')

        eachDay_arr = []

        for key in book_map:
            user_set = book_map.get(key)
            eachDay = EachDay(key,len(user_set),user_set)
            eachDay_arr.append(eachDay)
        #print eachDay_arr[0].printAll()
        eachDay_arr = sorted(eachDay_arr,key = lambda asd:asd.userNum,reverse=True)

        #print eachDay_arr[0].printAll()
        for i in range(0,10):
            output.write(eachDay_arr[i].printAll())
            output.write('\n')

        output.close()
    # for i in range(0,len(book_map)):
    #     if book_map[i][1] > 1:
    #         print i
    #print book_map