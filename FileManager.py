def addRecord(app, isbn, author, title):
    #this function is going to grow to make things shorted
    tempRecord = "{:0<10}".format(isbn)[:10]+"{:<16}".format(author)[:16]+"{:<24}".format(title)[:24]
    fl = open("./data/BookRecords.txt", "r+")
    indexSpot = len(app.indexIsbnList)
    if app.AVAIL:
        indexSpot = app.AVAIL.pop()
    else:
        tempRecord += "\n"
    fl.seek(52*indexSpot)
    fl.write(tempRecord)
    fl.close()
    app.indexIsbnList.append(["{:0<10}".format(isbn)[:10].strip(), indexSpot])
    app.indexIsbnList.sort(key=lambda x: x[0])
    app.indexTitleList.append(["{:<24}".format(title)[:24].strip(), indexSpot])
    app.indexTitleList.sort(key=lambda x: x[0])

def editRecordFile(app, isbn, author, title, index):
    tempRecord = "{:0<10}".format(isbn)[:10]+"{:<16}".format(author)[:16]+"{:<24}".format(title)[:24]
    fl = open("./data/BookRecords.txt", "r+")
    fl.seek(52*index)
    fl.write(tempRecord)
    fl.close()


def writeToIndexfile(isbnList, titleList):
    fl = open("./data/IndexIsbn.txt", "w")
    for x in isbnList:
        fl.write(x[0]+","+str(x[1])+"\n")
    fl.close()
    fl = open("./data/IndexTitle.txt", "w")
    for x in titleList:
        fl.write(x[0]+","+str(x[1])+"\n")
    fl.close()

def findRecordByIsbn(app, isbn):
    #this is going to change to a index file search
    with open("./data/BookRecords.txt", "r") as fl:
        for x in app.indexIsbnList:
            if x[0] == isbn:
                fl.seek(52 * int(x[1]))
                line = fl.readline()
                return [line[:10], line[10:26].strip(), line[26:51].strip()]
        return None

def findRecordByTitle(app, title):
    #this is going to change to a index file search
    with open("./data/BookRecords.txt", "r") as fl:
        for x in app.indexTitleList:
            if x[0] == title:
                fl.seek(52 * int(x[1]))
                line = fl.readline()
                return [line[:10], line[10:26].strip(), line[26:51].strip()]
        return None
            
    

def getAllRecords(app):
    fl = open("./data/BookRecords.txt", "r")
    recordNum = 0
    records =[]
    while True:
        temp = fl.readline()
        if recordNum in app.AVAIL:
            recordNum += 1
            continue
        if temp == "":
            break
        data = [temp[:10], temp[10:26].strip(), temp[26:51].strip()]
        records.append(data)
        recordNum += 1
    fl.close()
    return records

def loadIsbnIndexFile():
    fl = open("./data/IndexIsbn.txt", "r")
    indexList = []
    while True:
        temp = fl.readline()
        if temp == "":
            break
        temp = temp.strip().split(",")
        indexList.append([temp[0], int(temp[1])])
    fl.close()
    return indexList

def loadTitleIndexFile():
    fl = open("./data/IndexTitle.txt", "r")
    indexList = []
    while True:
        temp = fl.readline()
        if temp == "":
            break
        temp = temp.strip().split(",")
        indexList.append([temp[0], int(temp[1])])
    fl.close()
    return indexList

def crushRecordFile(app):
    with open("./data/BookRecords.txt", "r") as fl:
        records = fl.readlines()
    app.indexIsbnList = []
    app.indexTitleList = []
    with open("./data/BookRecords.txt", "w") as fl:
        lineNum = 0
        newNum = 0
        for record in records:
            if lineNum not in app.AVAIL:
                fl.write(record)
                app.indexIsbnList.append([record[:10], newNum])
                app.indexTitleList.append([record[26:51].strip(), newNum])
                newNum += 1
            lineNum += 1
        app.indexIsbnList.sort()
        app.indexTitleList.sort()
