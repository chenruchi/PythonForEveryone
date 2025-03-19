from tkinter import * #import function inside main package B=Button()
from tkinter import ttk #package ย่อย ttk ที่มี theme สวยกว่า

GUI = Tk()
GUI.title('โปรแกรมบันทึกความรู้ By BottleDev')
GUI.geometry('500x500')

L1 =ttk.Label(GUI,text='หัวข้อความรู้',font=('Angsana New',18))
L1.pack()

E1 = ttk.Entry(GUI,font=('Angsana New',20),width=50)
E1.pack() #(วางไว้ตรงกลาง บนลงล่าง)
#E1.place(x=300, y=300) #(วางตามตำแหน่ง x y ที่เรากำหนด)

L2 =ttk.Label(GUI,text='รายละเอียด',font=('Angsana New',18))
L2.pack()

T1 = Text(GUI,font=('Angsana New',18), height=8, width=56)
T1.pack()

B1 = ttk.Button(GUI,text='บันทึก')
B1.pack(pady=10, ipadx=20, ipady=10)


GUI.mainloop() #เพื่อให้โปรแกรม run อยู่ตลอด จนกว่าเราจะกดปิด