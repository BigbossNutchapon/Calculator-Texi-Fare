from tkinter import *
import math

#สร้างTkinter หน้าหลัก
root = Tk()
root.title("โปรแกรมคำนวณค่าแท็กซี่")

root.geometry("380x450+700+100")
root.configure(bg="#fff")
root.resizable(False,False)

#set font stype
FONT_TITLE = ('Microsoft Yahei UI Light',18)
FONT_DEFULT = ('Microsoft Yahei UI Light')
#set color font
FONT_COLOR_DEFULT = "black"

#function checkfile ถ้าเครื่องuser 1ยังไม่มีไฟล์historeyจะทำการสร้างใหม่
def checkfile():
    try:
        #หาไฟล์
        fr = open("History.txt","r",encoding="utf-8")
        fr.read()
        fr.close()
    except FileNotFoundError:
        #สร้างfile
        fw = open("History.txt","w",encoding="utf-8")
        fw.close()
checkfile()

def mainpage():
    #สร้างframe พื้นที่การทำงาน
    frame = Frame(root,width=400,height=400,bg='white')
    frame.place(x=10,y=15)

    #label แสดงโปรแกรมแปลงค่าอุณภูมิ บนหัวโปรแกรม
    heading = Label(frame,text='โปรแกรมคำนวณค่าโดยสารแท็กซี่',fg='#4169E1',bg='white',font=FONT_TITLE)
    heading.place(x=10,y=5)
    dev = Label(frame,text='By:Nutchapon Kitkram',fg="#808080",bg='white',font=(FONT_DEFULT,9))
    dev.place(x=10,y=40)
    #บรรทัดรับค่าอุณหภูมิ
    #function เวลาคลิกช่องกรอกแล้วตัวอักษรในช่องหายไปให้พร้อมกรอก ใช้ .delete เพื่อล้างค่า
    def on_enter(e):
        user.delete(0,END)

    # เมื่อuser ยังไม่กรอก ค่ายังว่าง เมื่อกดที่อื่นคำว่ากรอกอุณหภูมิ(ex.36C or 245F) ก็จะกลับมา ใช้ .get รับค่ามาเช็ค ถ้ายังไม่ได้ใส่อะไร ให้แสดงคำที่เซ็ตไว้เหมือนเดิม
    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0,'กรอกระยะทาง')

    #set ค่าตัวแปรtemp ให้เป็น stringVar
    dist = IntVar()

    #แสดงคำว่ากรอกอุณภูมิด้วยlabel ขนาดฟอนต์13
    label1 = Label(frame,text='กรอกระยะทาง',fg='black',bg='white',font=('Microsoft Yahei UI Light',10),padx=5)
    label1.place(x=10,y=80)

    #ช่องรับinput จาก user ตั้งให้ตัวอักษรอยู่ตรงกลาง และไม่มีกรอบ
    user = Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',12),justify='left',textvariable=dist)
    user.place(x=20,y=110)

    #set ค่าในช่องที่userกรอก เพื่อยกตัวอย่าง ด้วย.insert
    user.insert(0,'กรอกระยะทาง')

    #เรียกfunction เมื่อกดแล้วจะล้างตัวหนังสือให้พร้อมป้อน ด้วย.bind
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    #สร้างเส้นข้างล่างของentry ด้วยFrame
    Frame(frame,width=325,height=2,bg='#57a1f8').place(x=20,y=137)

    #บรรทัดแสดงผลลัพธ์
    #แสดงคำว่าผลการคำนวณด้วยlabel ขนาดฟอนต์13
    label2 = Label(frame,text='ผลการคำนวณ :',fg='black',bg='white',font=('Microsoft Yahei UI Light',10),padx=5)
    label2.place(x=10,y=160)

    #สร้างช่องแสดงผลลัพธ์
    display = Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',12),justify='left')
    display.place(x=20,y=190)

    #สร้างเส้นข้างล่างของentry ด้วยFrame
    Frame(frame,width=325,height=2,bg='#57a1f8').place(x=20,y=215)
    
    def history():
        clearpage()
        heading = Label(root,text='ประวัติการคำนวณ',fg='#4169E1',bg='white',font=FONT_TITLE)
        heading.place(x=10,y=5)
        frame = Frame(root,width=380,height=370,bg='white')
        frame.place(x=5,y=40)
        fr = open("History.txt","r",encoding="utf-8")
        labelHis = Label(frame,text=fr.read(),fg='black',bg='white',font=('Microsoft Yahei UI Light',11),pady=5,justify=LEFT)
        labelHis.place(y=0,x=2)
    def clearpage():
        frame.destroy()
    #function
    def taxi():
        distance = dist.get() #KM
        distance2 = distance - math.floor(distance)
        distance = math.floor(distance)

        box = 0
        check = {10:6.5, 20:7.5, 40:8.0, 60:9.0, 80:10.5}

        for i in range(1,distance+1):
            if i == 1:
                tx = 35
            elif i > 1 and i <= 10:
                tx = 5.5
            elif i > 10 and i <= 20:
                tx = 6.5
            elif i > 20 and i <= 40:
                tx = 7.5
            elif i > 40 and i <= 60:
                tx = 8.0
            elif i > 60 and i <= 80:
                tx = 9.0
            elif i > 80:
                tx = 10.5
            else:
                print("error")
            box += tx
        #หากระยะทาง อยู่ในcheck จะดึงราคาสุดท้ายมาคำนวณ 
        if distance in check:
            tx = check[distance]
            #จะเอาค่าสุดท้ายที่เช็ค มาคูณกับtx ที่เซ็ตไว้ในdict
            extra = distance2 * tx
        else:
            #ในกรณีไม่อยู๋ในค่าที่เซ้ตไว้ สามารถใช้ค่าtx จะลูปได้เลย
            tx = tx
            extra = distance2 * tx
        calculate = round(box + extra)
        result = str(dist)+" = "+str(calculate)+" บาท"
        fw = open("History.txt", "a", encoding="utf-8")
        fw.writelines(str(result)+"\n")
        fw.close()
    #ปุ่มหน้าแรก คำนวณ ดูประวัติ และออกจากโปรแกรม
    Button(frame,width=20,pady=7,text='คำนวณ',bg='#4169E1',fg='white',border=0,cursor='hand2',font=('Microsoft Yahei UI Light',11),command=taxi).place(x=80,y=240)
    Button(frame,width=20,pady=7,text='ดูประวัติ',bg='#C0C0C0',fg='black',border=0,cursor='hand2',font=('Microsoft Yahei UI Light',11),command=history).place(x=80,y=290)
    Button(frame,width=20,pady=7,text='ออกจากโปรแกรม',bg='red',fg='white',border=0,cursor='hand2',font=('Microsoft Yahei UI Light',11),command=root.quit()).place(x=80,y=340)
def main():
    mainpage()
main()
root.mainloop()