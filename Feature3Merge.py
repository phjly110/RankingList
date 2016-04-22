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

def merge3Feature(date,mergeDay):
    book_map = {}
    bookAdd_map = {}

    for j in range(mergeDay):
        day = int(date.split('-')[2])-j
        if day < 10:
            date_str = date[:-2] + '0' +str(day)
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
                    #feature_list.extend(featureadd_list)
                    book_map[bookId] = feature_list
                    if bookId == 'b0026235':
                        print feature_list
                    bookAdd_map[bookId] = featureadd_list
            else:

                if bookAdd_map.get(bookId):
                    feature_list = bookAdd_map.get(bookId)
                    for i in range(0,len(feature_str)):
                        feature_list[i] = float(feature_list[i])+float(feature_str[i])
                    #feature_list.extend(featureadd_list)
                    bookAdd_map[bookId] = feature_list
                    if bookId == 'b0026235':
                        print book_map.get(bookId)
                else:
                    feature_list = []
                    for i in range(0,len(feature_str)):
                        feature_list.append(float(feature_str[i]))
                    #feature_list.extend(featureadd_list)
                    bookAdd_map[bookId] = feature_list

            line = f.readline()

        f.close()
        if j == 2:
            for key in bookAdd_map:
                if key in book_map:
                    feature_list = book_map[key]
                    if key == 'b0026235':
                        print feature_list
                    feature_list.extend(bookAdd_map[key])
                    if key == 'b0026235':
                        print feature_list
                    book_map[key] = feature_list
                else:
                    feature_list = []
                    for i in range(18):
                        feature_list.append(0)
                    feature_list.extend(bookAdd_map[key])
                    book_map[key] = feature_list
            book_map = completionFeatureList(book_map,18*2)

        if j == 6:
            for key in bookAdd_map:
                if key in book_map:
                    feature_list = book_map[key]
                    if key == 'b0026235':
                        print feature_list
                    feature_list.extend(bookAdd_map[key])
                    if key == 'b0026235':
                        print feature_list
                    book_map[key] = feature_list
                else:
                    feature_list = []
                    for i in range(36):
                        feature_list.append(0)
                    feature_list.extend(bookAdd_map[key])
                    book_map[key] = feature_list
            book_map = completionFeatureList(book_map,18*3)

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

        if int(feature_list[11+36]) == 0:
            for i in range(36+13,36+17):
                feature_list[i] = 0
        else:
            feature_list[13+36] = round(float(feature_list[10+36])/feature_list[11+36],5)
            feature_list[14+36] = round(float(feature_list[12+36])/feature_list[11+36],5)
            feature_list[15+36] = round(float(feature_list[1+36])/feature_list[11+36],5)
            feature_list[16+36] = round(float(feature_list[3+36])/feature_list[11+36],5)
            feature_list[17+36] = round(float(feature_list[5+36])/feature_list[11+36],5)
        book_map[key] = feature_list

        a = bookFeature(key,book_map[key])
        bookFeatureArr.append(a)

    output = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/feature_3Merge/'+date+'_feature','w')

    for i in range(len(bookFeatureArr)):
        output.write(bookFeatureArr[i].printAll())
        output.write('\n')

    output.close()

    return 1

def run():
    date = '2013-07-07'
    merge3Feature(date,7)

if __name__ == '__main__':
    run()