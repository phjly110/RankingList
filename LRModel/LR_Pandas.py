# _*_ coding:utf-8 _*_
import pandas as pd

def run():
    df = pd.read_csv("/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureEngineering/Combine_csv/bank.csv")
    print df.mean()
    #print df.head()
    #print df.describe()
    #print pd.crosstab(df['label'],df['fea26'],rownames=['label'])
    #dummy_ranks = pd.get_dummies(df['fea1'], prefix='fea1')
    #print dummy_ranks

    return 1

if __name__ == '__main__':
    run()