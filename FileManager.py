def addRecord(isbn, author, title):
    #this function is going to grow to make things shorted
    tempRecord = "{:<10}".format(isbn)[:10]+"{:<16}".format(author)[:16]+"{:<24}".format(title)[:24]+"\n"
    print(tempRecord)
    fl = open("./data/BookRecords.txt", "a")
    fl.write(tempRecord)
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
            print("Record doesn't exist")
            break
        print(data)
        records.append(data)
    fl.close()
    return records
