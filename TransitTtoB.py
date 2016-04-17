# _*_ coding:utf-8 _*_

def run():
    #f = open()
    yearAndMonth = "2013-07-"

    for i in range(0,30):
        i = i+1
        #book_map = {}
        #line = f.readline()
        if i < 10:
            date = yearAndMonth + "0" + str(i)
        else:
            date = yearAndMonth + str(i)
        f = open("/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/SplitByDay/" + date,'r')
        lines = f.readlines()
        for i in range(0,len(lines)):
            if '\t' in lines[i]:
                lines[i] = lines[i].replace('\t',' ')
        open("/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/SplitByDay/" + date,'w').writelines(lines)

        #f.writelines(li)
        #f.close()

if __name__ == '__main__':
    run()