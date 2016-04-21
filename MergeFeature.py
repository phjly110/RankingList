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


def completionFeatureList(map,list_len):     #补全特征list,当书籍出现,但前一个特征中却没有的情况下
    for key in map:
        feature_list = map[key]
        #print len(feature_list)
        if len(feature_list) != int(list_len):     #list_len是所有特征相加的个数
            for i in range(len(feature_list),list_len):
                feature_list.append(0)
            map[key] = feature_list
    return map


def mergeFeature(date, mergeDay):
    book_map = {}


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
            feature_str = line.split('[')[1].split(']')[0].split(',')
            if j == 0:
                featurepre_list = []
                featureadd_list = []
                for i in range(0,len(feature_str)):
                    featureadd_list.append(float(feature_str[i]))
                    featurepre_list.append(float(feature_str[i]))

                if book_map.get(bookId):
                    print 'have same bookId in first day!'

                else:
                    feature_list = []
                    feature_list.extend(featurepre_list)
                    feature_list.extend(featureadd_list)
                    book_map[bookId] = feature_list
            else:

                if book_map.get(bookId):
                    feature_list = book_map.get(bookId)
                    for i in range(18,18+len(feature_str)):
                        feature_list[i] = float(feature_list[i])+float(feature_str[i-18])
                    #feature_list.extend(featureadd_list)
                    book_map[bookId] = feature_list
                else:
                    feature_list = []
                    for i in range(18):
                        feature_list.append(0)
                    for i in range(0,len(feature_str)):
                        feature_list.append(float(feature_str[i]))
                    #feature_list.extend(featureadd_list)
                    book_map[bookId] = feature_list

            line = f.readline()

        f.close()

    book_map = completionFeatureList(book_map,18*2)

    for key in book_map:
        feature_list = book_map[key]


    bookFeatureArr = []
    for key in book_map:
        feature_list = book_map[key]
        if int(feature_list[11+18]) == 0:
            for i in range(18+13,18+17):
                feature_list[i] = 0
        else:
            feature_list[13+18] = round(float(feature_list[10+18])/feature_list[11+18],5)
            feature_list[14+18] = round(float(feature_list[12+18])/feature_list[11+18],5)
            feature_list[15+18] = round(float(feature_list[1+18])/feature_list[11+18],5)
            feature_list[16+18] = round(float(feature_list[3+18])/feature_list[11+18],5)
            feature_list[17+18] = round(float(feature_list[5+18])/feature_list[11+18],5)
        book_map[key] = feature_list

        a = bookFeature(key,book_map[key])
        bookFeatureArr.append(a)

    output = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureMerge/'+date+'_feature','w')

    for i in range(len(bookFeatureArr)):
        output.write(bookFeatureArr[i].printAll())
        output.write('\n')

    output.close()

    return 1

def run():
    date = '2013-07-30'
    mergeFeature(date, 3)

if __name__ == '__main__':
    run()