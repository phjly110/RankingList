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



def addDwellTimeFeatureList(map,dwellTime_map,list_len):
    for key in dwellTime_map:
        if map.get(key):
            feature_list = map.get(key)
            dwellTime = dwellTime_map.get(key)
            feature_list.append(dwellTime)
            map[key] = feature_list
        else:
            print key
            feature_list = []
            for i in range(0,list_len):          #若这本书之前没有出现在特征list中,需要补全之前的特征个数
                feature_list.append(0)
            dwellTime = dwellTime_map.get(key)
            feature_list.append(dwellTime)
            map[key] = feature_list
    return map


#map是bookFeature的一个暂时存放的map,add_map是新加特征的map,
#list_len是需补全0的长度.
#这个函数只用来增加eventID=1~7的统计量(例如:加入书架次数,加入书架人数(加入书架的阅读者的去重))
#并不能对阅读时长特征进行添加
def addFeatureList(map,add_map,list_len):
    for key in add_map:
        if map.get(key):
            feature_list = map.get(key)
            feature_list.append(len(add_map[key]))
            feature_list.append(len(list(set(add_map[key]))))
            map[key] = feature_list
        else:
            feature_list = []
            for i in range(0,list_len):          #若这本书之前没有出现在特征list中,需要补全之前的特征个数
                feature_list.append(0)
            feature_list.append(len(add_map[key]))
            feature_list.append(len(list(set(add_map[key]))))
            map[key] = feature_list
    return map

def completionFeatureList(map,list_len):     #补全特征list,当书籍出现,但前一个特征中却没有的情况下
    for key in map:
        feature_list = map[key]
        #print len(feature_list)
        if len(feature_list) != int(list_len):     #list_len是所有特征相加的个数
            for i in range(len(feature_list),list_len):
                feature_list.append(0)
            map[key] = feature_list
    return map

def run():
    f_date = '2013-07-30'
    f = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/SplitByDay/' + f_date)
    book_map = {}
    add_map = {}
    del_map = {}
    download_map = {}
    clickCover_map = {}
    clickCatalog_map = {}
    dwellTimeCount_map = {}
    dwellTime_map = {}
    #add_num = 0
    line = f.readline()
    while line:
        userId,bookId,eventId,time = line.split(',')
        date,dwellTime = time.split(' ')     #由于eventID=7的时候需要用到dwellTime,而其余eventID不需要用到时间戳,注意其余的eventID分割的第二项不是dwellTime
        if date == '2013/07/30':
            if eventId == '1':
                if add_map.get(bookId):
                    user_set = add_map.get(bookId)
                    user_set.append(userId)
                    add_map[bookId] = user_set
                else:
                    user_set = []
                    user_set.append(userId)
                    add_map[bookId] = user_set
            elif eventId == '2':
                if del_map.get(bookId):
                    user_set = del_map.get(bookId)
                    user_set.append(userId)
                    del_map[bookId] = user_set
                else:
                    user_set = []
                    user_set.append(userId)
                    del_map[bookId] = user_set
            elif eventId == '3':
                if download_map.get(bookId):
                    user_set = download_map.get(bookId)
                    user_set.append(userId)
                    download_map[bookId] = user_set
                else:
                    user_set = []
                    user_set.append(userId)
                    download_map[bookId] = user_set
            elif eventId == '4':
                if clickCover_map.get(bookId):
                    user_set = clickCover_map.get(bookId)
                    user_set.append(userId)
                    clickCover_map[bookId] = user_set
                else:
                    user_set = []
                    user_set.append(userId)
                    clickCover_map[bookId] = user_set
            elif eventId == '6':
                if clickCatalog_map.get(bookId):
                    user_set = clickCatalog_map.get(bookId)
                    user_set.append(userId)
                    clickCatalog_map[bookId] = user_set
                else:
                    user_set = []
                    user_set.append(userId)
                    clickCatalog_map[bookId] = user_set
            elif eventId == '7':
                if dwellTimeCount_map.get(bookId):
                    user_set = dwellTimeCount_map.get(bookId)
                    user_set.append(userId)
                    dwellTimeCount_map[bookId] = user_set
                    dwellTime_map[bookId] = dwellTime_map[bookId] + int(dwellTime)   #取出已有的阅读时长并加上这次dwellTime
                else:
                    user_set = []
                    user_set.append(userId)
                    dwellTimeCount_map[bookId] = user_set
                    dwellTime_map[bookId] = int(dwellTime)    #把阅读时长加入dwellTime_map中去
        line = f.readline()
    f.close()

    book_arr = []

    #——————————————————————增加直接得到的特征——————————————————————
    #增加add的特征
    for key in add_map:
        feature_list = []
        feature_list.append(len(add_map[key]))
        feature_list.append(len(list(set(add_map[key]))))
        book_map[key] = feature_list

    #增加del的特征
    book_map = addFeatureList(book_map,del_map,2)
    #增加del后,补全特征list的0项
    book_map = completionFeatureList(book_map,4)
    #增加download特征
    book_map = addFeatureList(book_map,download_map,4)
    #增加download后,补全特征list的0项
    book_map = completionFeatureList(book_map,6)
    #增加clickCover特征
    book_map = addFeatureList(book_map,clickCover_map,6)
    #增加clickCover后,补全特征list的0项
    book_map = completionFeatureList(book_map,8)
    #增加clickCatalog特征
    book_map = addFeatureList(book_map,clickCatalog_map,8)
    #增加clickCatalog后,补全特征list的0项
    book_map = completionFeatureList(book_map,10)
    #增加dwellTimeCount特征
    book_map = addFeatureList(book_map,dwellTimeCount_map,10)
    #增加dwellTimeCount后,补全特征list的0项
    book_map = completionFeatureList(book_map,12)
    #增加dwellTime特征
    book_map = addDwellTimeFeatureList(book_map,dwellTime_map,12)
    #增加dwellTime后,补全特征list的0项
    book_map = completionFeatureList(book_map,13)
    #------------------以下是增肌转换率类的特征————————————————————————————
    #增加特征(阅读量/阅读人数)、（阅读时长/阅读人数）、
    # （加入书架人数/阅读人数）、（删除书架人数/阅读人数）、
    # （下载人数/阅读人数）
    for key in book_map:
        feature_list = book_map[key]
        readCount = feature_list[10]         #阅读量
        readPeopleNum = feature_list[11]     #阅读人数
        readDwellTime = feature_list[12]     #阅读时长
        addPeopleNum = feature_list[1]       #加入书架人数
        delPeopleNum = feature_list[3]       #删除书架人数
        downloadPeopleNum = feature_list[5]  #下载人数
        if readPeopleNum == 0:
            for i in range(0,5):
                feature_list.append(0)
        else:
            feature_list.append(round(float(readCount)/readPeopleNum,5))
            feature_list.append(round(float(readDwellTime)/readPeopleNum,5))
            feature_list.append(round(float(addPeopleNum)/readPeopleNum,5))
            feature_list.append(round(float(delPeopleNum)/readPeopleNum,5))
            feature_list.append(round(float(downloadPeopleNum)/readPeopleNum,5))
        book_map[key] = feature_list

    #将map转换为bookFeature类存储
    for key in book_map:
        feature_list = book_map[key]
        if len(feature_list) != 18:
            print key
        book_feature = bookFeature(key,feature_list)
        book_arr.append(book_feature)

    book_arr = sorted(book_arr, key = lambda asd:asd.feature_arr[0],reverse = True)
    output = open('/Users/phj/Documents/Postgraduate/BookData/BooksPredict/OriginalData/featureMatrix/' + f_date +'_feature18','w')

    for key in book_arr:
        output.write(key.printAll())
        output.write('\n')

    output.close()

if __name__ == '__main__':
    run()