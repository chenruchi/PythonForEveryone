import csv

def writecsv(data):
    # data = ['John',14,500] 
    with open('knowledge.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) #FW = File Writer
        fw.writerow(data)

    #ถ้า Error ให้ใช้วิธีนี้
    # filename = 'c:\\User\\Uncle Engineer\\Desktop\\Pythonforeveryone\\knowledge.csv'
    # with open('filename',newline='',encoding='utf-8') as file:
    #จะไม่ Error ถ้าใส่ path แบบเต็ม และ ใส่ \\


def readcsv():
    with open('knowledge.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
        print(data)

readcsv()

# d = ['Ericssen',45,800] 
# writecsv(d)