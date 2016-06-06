# _*_ coding:utf-8 _*_

import math
import matplotlib.pyplot as plt

#画曲线
if __name__ == "__main__":
    x = [10,20,30,40,50]
    #Batch
    #y1 = [48.539,69.332,75.826,80.845,83.092]
    #y2 = [48.539,34.723,25.396,20.223,16.604]
    #SGD
    y1 = [35.839,46.057,55.223,62.973,67.294]
    y2 = [35.239,23.844,18.638,14.492,13.931]

    plt.plot(x,y1,'r-', linewidth=3, label = 'Accuracy')
    plt.plot(x,y1,'b*', markersize=15, alpha=0.75)
    plt.plot(x,y2,'g-', linewidth=3, label = 'Recall')
    plt.plot(x,y2,'y*', markersize=15, alpha=0.75)
    # a = [x[20], x[175]]
    # b = [y[20], y[175]]
    # plt.plot(a, b, 'g-', linewidth=2)
    # plt.plot(a, b, 'b*', markersize=15, alpha=0.75)
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.xlabel('Threshold')
    plt.ylabel('Percentage(%)')
    #plt.title('BatchSG')
    plt.title('SGD')
    plt.show()