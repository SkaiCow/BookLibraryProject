def addRecord(app, isbn, author, title):
    #this function is going to grow to make things shorted
    tempRecord = "{:<10}".format(isbn)[:10]+"{:<16}".format(author)[:16]+"{:<24}".format(title)[:24]+"\n"
    fl = open("./data/BookRecords.txt", "a")
    fl.write(tempRecord)
    fl.close()
    app.indexIsbnList.append([isbn, str(len(app.indexIsbnList))])
    app.indexIsbnList.sort(key=lambda x: x[0])
    app.indexTitleList.append([title, str(len(app.indexTitleList))])
    app.indexTitleList.sort(key=lambda x: x[0])

def writeToIndexfile(isbnList, titleList):
    fl = open("./data/IndexIsbn.txt", "w")
    for x in isbnList:
        fl.write(x[0]+","+x[1]+"\n")
    fl.close()
    fl = open("./data/IndexTitle.txt", "w")
    for x in titleList:
        fl.write(x[0]+","+x[1]+"\n")
    fl.close()

def findRecordByIsbn(isbn):
    #this is going to change to a index file search
    fl = open("./data/BookRecords.txt", "r")
    recordNum = 0
    while True:
        temp = fl.readline()
        if temp[:10] == isbn:
            print("Record exist")
            break
        if temp == "":
            print("Record doesn't exist")
            break
        recordNum += 1
    fl.close()

def getAllRecords():
    fl = open("./data/BookRecords.txt", "r")
    recordNum = 0
    records =[]
    while True:
        temp = fl.readline()
        data = [temp[:10], temp[10:26].strip(), temp[26:51].strip()]
        if temp == "":
            break
        records.append(data)
    fl.close()
    return records

def loadIsbnIndexFile():
    fl = open("./data/IndexIsbn.txt", "r")
    indexList = []
    while True:
        temp = fl.readline()
        if temp == "":
            break
        indexList.append(temp.strip().split(","))
    fl.close()
    return indexList

def loadTitleIndexFile():
    fl = open("./data/IndexTitle.txt", "r")
    indexList = []
    while True:
        temp = fl.readline()
        if temp == "":
            break
        indexList.append(temp.strip().split(","))
    fl.close()
    return indexList
