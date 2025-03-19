from tkinter import * #import function inside main package B=Button()
from tkinter import ttk #package ย่อย ttk ที่มี theme สวยกว่า
import csv
import os

path = os.getcwd()
#print('PATH: ', path) #แสดง path ที่ ไฟล์นี้อยู่

noteicon = os.path.join(path, 'noteicon.png')

def writecsv(data):
    # data = ['John',14,500] 
    csvfile = os.path.join(path,'knowledge.csv')
    with open(csvfile,'a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) #FW = File Writer
        fw.writerow(data)

GUI = Tk()
GUI.title('โปรแกรมบันทึกความรู้ By BottleDev')
GUI.geometry('800x800')
GUI.iconbitmap(noteicon)

F1 = Frame(GUI)
F1.place(x=20, y=50)

L1 = ttk.Label(F1, text='หัวข้อความรู้',font=('Angsana New',18))
L1.pack(pady=20)

v_title = StringVar()
E1 = ttk.Entry(F1,textvariable=v_title,font=('Angsana New',20),width=50)
E1.pack() #(วางไว้ตรงกลาง บนลงล่าง)
#E1.place(x=300, y=300) #(วางตามตำแหน่ง x y ที่เรากำหนด)

L2 =ttk.Label(F1,text='รายละเอียด',font=('Angsana New',18))
L2.pack()

T1 = Text(F1,font=('Angsana New',18), height=8, width=56)
T1.pack()

def save():
    title = v_title.get()
    textbox = T1.get(1.0,"end-1c")
    print('-------')
    print(title)
    print('-------')
    print(textbox)
    print('-------')

    data = [title,textbox]
    writecsv(data)

    v_title.set('') #clear data after save
    T1.delete('1.0',END) #clear textboxs after save

B1 = ttk.Button(F1,text='บันทึก',command=save)
B1.pack(pady=10, ipadx=20, ipady=10)

#####Button flashcard#####

def readcsv():
    with open('knowledge.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
        return data

knowledgelist = readcsv()
#print(knowledgelist) 

global countindex #เป็นตัวแปร global
countindex = 0

def Flashcard():
    knowledgelist = readcsv()
    GUI2 = Toplevel()
    GUI2.title('ทบทวนความรู้')
    GUI2.geometry('500x450')

    vtext_title = StringVar()
    vtext_detail = StringVar()
    title = ttk.Label(GUI2,textvariable=vtext_title,font=('Angsana New',20,'bold'))
    title.pack()
    vtext_title.set(knowledgelist[0][0])
    detail = ttk.Label(GUI2,textvariable=vtext_detail,font=('Angsana New',14))
    detail.pack()
    vtext_detail.set(knowledgelist[0][1].replace('\r',' '))

    def Prev():
        global countindex
        if countindex == 0:
            countindex = countindex
        else:
            countindex = countindex - 1

        #set text
        print('CountIndex: ',countindex)
        vtext_title.set(knowledgelist[countindex][0])
        vtext_detail.set(knowledgelist[countindex][1].replace('/r',''))
    
    def Next():
        global countindex
        if countindex == (len(knowledgelist)-1):
            countindex = len(knowledgelist)-1
        else:
            countindex = countindex + 1

        #set text
        print('CountIndex: ',countindex)
        vtext_title.set(knowledgelist[countindex][0])
        vtext_detail.set(knowledgelist[countindex][1].replace('/r',''))
    


    BPrev = ttk.Button(GUI2,text='<<',command=Prev)
    BPrev.place(x=140, y=350)
    BNext = ttk.Button(GUI2,text='>>',command=Next)
    BNext.place(x=260, y=350)
    

    GUI2.mainloop()



notebutton = os.path.join(path, 'note.png')
noteicon = PhotoImage(file=notebutton)

BFlashcard = ttk.Button(GUI,image=noteicon,command=Flashcard)
BFlashcard.place(x=450, y=20)

GUI.mainloop() #เพื่อให้โปรแกรม run อยู่ตลอด จนกว่าเราจะกดปิด