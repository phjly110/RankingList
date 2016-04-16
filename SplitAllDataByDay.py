# _*_ coding:utf-8 _*_



def run():

    yearAndMonth = '2013/07/'
    #line = f.readline()
    for i in range(1,31):
        print i
        f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/filterDwelltime')

        if i < 10:
            date = yearAndMonth + "0" + str(i)
        else:
            date = yearAndMonth + str(i)

        output = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/SplitByDay/'+date.replace('/','-'),'a')

        line = f.readline()

        while line:
            #filterDwelltime是'/t',其余是' '
            timeStamp = line.split('\t')[0].split(',')[-1]
            #print timeStamp
            if timeStamp == date:
                #output.write(line)
                #把filterDwelltime输入进行改变写入,对应的数据标号为7
                line = line.replace(',2013',',7,2013')
                output.write(line)
            line = f.readline()

        output.close()
        f.close()





if __name__ == '__main__':
    run()