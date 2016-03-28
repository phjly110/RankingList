# _*_ coding:utf-8 _*_

import matplotlib.pyplot as plt

def run():
    f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/FilterByDay/AllReadSituation/allReadSituation')
    line = f.readline()
    y_all = []
    color_arr = ['b','c','g','k','m','r','y','b','c','g']
    while line:
        date, readNum = line.split(',',1)
        readNum = readNum.split('[')[1].split(']')[0].split(',')
        #print readNum
        x = [i for i in range(1,11)]
        y = [int(readNum[i]) for i in x]
        y_all.append(y)
        print y

        #plt.plot(x,y,'r-',linewidth=1, label='readTread')
        line = f.readline()

    x = [i for i in range(1,31)]
    for i in range(0,len(y_all[0])):
        one_line = [int(y_all[j][i]) for j in range(0,len(y_all))]
        plt.plot(x,one_line,color_arr[i],linewidth=1, label='readTread')

    plt.grid(True)
    plt.xlabel('x_Day')
    plt.ylabel('Reading Quantity')
    plt.show()




if __name__ == '__main__':
    run()