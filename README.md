
''' Using Python and MySQL, I created a full stack programmes
I used the following libraries: 
1) Tkinter,
2) mysql.connector
3) time.
To carry out the smooth functioning of codes, various functions and arithmetic operations were used. '''


Program 1:
Menu systems
import tkinter
from tkinter import *
from tkinter import messagebox
import time
import mysql.connector as my
def exit():
    root.destroy()
def bill():
    global pl,pb,pt,dt,sp,pr,br,rh,rf,hs,sc,ts,ms,pd,mp
    global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o
    pl=a.get()
    if pl>0:
        qw=350*pl
    else:
        pl=0
        qw=0
    pb=b.get()
    if pb>0:
        we=320*pb
    else:
        pb=0
        we=0
    pt=c.get()
    if pt>0:
        er=375*pt
    else:
        pt=0
        er=0
    dt=d.get()
    if dt>0:
        rt=275*dt
    else:
        dt=0
        rt=0
    sp=e.get()
    if sp>0:
        ty=320*sp
    else:
        sp=0
        ty=0
    pr=f.get()
    if pr>0:
        yu=20*pr
    else:
        pr=0 
        yu=0
    br=g.get()
    if br>0:
        ui=30*br
    else:
        br=0 
        ui=0
    rh=h.get()
    if rh>0:
        io=60*rh
    else:
        rh=0 
        io=0
    rf=i.get()
    if rf>0:
        op=120*i
    else:
        rf=0 
        op=0
    hs=j.get()
    if hs>0:
        pa=180*hs
    else:
        hs=0 
        pa=0
    sc=k.get()
    if sc>0:
        ad=170*sc
    else:
        sc=0 
        ad=0
    ts=l.get()
    if ts>0:
        df=170*ts
    else:
        ts=0 
        df=0
    ms=m.get()
    if ms>0:
        fg=190*ms
    else:
        ms=0
        fg=0
    pd=n.get()
    if pd>0:
        gh=20*pd
    else:
        pd=0 
        gh=0
    mp=o.get()
    if mp>0:
        hj=30*mp
    else:
        mp=0 
        hj=0
    q=(pl+pb+pt+dt+sp+pr+br+rh+rf+hs+sc+ts+ms+pd+mp)
    sub=(qw+we+er+rt+ty+yu+ui+io+op+pa+ad+df+fg+gh+hj)
    CGST=((sub*9)/100)
    SGST=((sub*9)/100)
    tx=CGST+SGST
    ser=((sub*4)/100)
    tl=sub+tx+ser
    datb=my.connect(host="localhost",user="root",passwd="Mahir@7314",database="pbm")
    curs=datb.cursor()
    curs.execute("insert into order1(quantity,tax,service,total) values (%s,%s,%s,%s)",(q,tx,ser,tl))
    datb.commit()
    st.set(sub)
    total.set(tl)
    qty.set(q)
    tax.set(tx)
    service.set(ser)
        
root=Tk()
root.title("punjab grill")
root.geometry("1920x1080")
root.attributes("-fullscreen",True)
a=IntVar()
b=IntVar()
c=IntVar()
d=IntVar()
e=IntVar()
f=IntVar()
g=IntVar()
h=IntVar()
i=IntVar()
j=IntVar()
k=IntVar()
l=IntVar()
m=IntVar()
n=IntVar()
o=IntVar()
qty=StringVar()
total=StringVar()
st=StringVar()
service=StringVar()
tax=StringVar()
lbl1=Label(root,text="welcome to Punjab Grill",font=('Times New Roman',36,('bold','italic')),fg='red').grid(row=0,column=6)
localtime=time.asctime(time.localtime(time.time()))
lb12=Label(root,text=localtime,font=('Times New Roman',28,('bold','underline'))).grid(row=2,column=6)
lbl3=Label(root,text="Menu",font=('Times New Roman',28,('bold','underline'))).grid(row=4,column=6)
lbl4=Label(root,text="items",font=('Times New Roman',18,('bold','underline'))).grid(row=6,column=5)
lbl5=Label(root,text="price",font=('Times New Roman',18,('bold','underline'))).grid(row=6,column=6)
lbl6=Label(root,text="Quantity",font=('Times New Roman',18,('bold','underline'))).grid(row=6,column=7)

lbl7=Label(root,text="paneer lababdaar",font=('Times New Roman',14,'bold')).grid(row=8,column=5)
lbl8=Label(root,text="350",font=('Times New Roman',14,'bold')).grid(row=8,column=6)
et1=Entry(root,textvariable=a,font=('Times New Roman',14,'bold')).grid(row=8,column=7)

lbl9=Label(root,text="paneer butter masala",font=('Times New Roman',14,'bold')).grid(row=9,column=5)
lbl10=Label(root,text="320",font=('Times New Roman',14,'bold')).grid(row=9,column=6)
et2=Entry(root,textvariable=b,font=('Times New Roman',14,'bold')).grid(row=9,column=7)

lbl11=Label(root,text="paneer tikka",font=('Times New Roman',14,'bold')).grid(row=10,column=5)
lbl12=Label(root,text="375",font=('Times New Roman',14,'bold')).grid(row=10,column=6)
et3=Entry(root,textvariable=c,font=('Times New Roman',14,'bold')).grid(row=10,column=7)

lbl13=Label(root,text="dal tadkha",font=('Times New Roman',14,'bold')).grid(row=11,column=5)
lbl14=Label(root,text="275",font=('Times New Roman',14,'bold')).grid(row=11,column=6)
et4=Entry(root,textvariable=d,font=('Times New Roman',14,'bold')).grid(row=11,column=7)

lbl15=Label(root,text="shezwan paneer fry",font=('Times New Roman',14,'bold')).grid(row=12,column=5)
lbl16=Label(root,text="320",font=('Times New Roman',14,'bold')).grid(row=12,column=6)
et5=Entry(root,textvariable=e,font=('Times New Roman',14,'bold')).grid(row=12,column=7)

lbl17=Label(root,text="plain roti",font=('Times New Roman',14,'bold')).grid(row=13,column=5)
lbl18=Label(root,text="20",font=('Times New Roman',14,'bold')).grid(row=13,column=6)
et6=Entry(root,textvariable=f,font=('Times New Roman',14,'bold')).grid(row=13,column=7)

lbl18=Label(root,text="butter roti",font=('Times New Roman',14,'bold')).grid(row=14,column=5)
lbl19=Label(root,text="30",font=('Times New Roman',14,'bold')).grid(row=14,column=6)
et7=Entry(root,textvariable=g,font=('Times New Roman',14,'bold')).grid(row=14,column=7)

lbl20=Label(root,text="rice(half)",font=('Times New Roman',14,'bold')).grid(row=15,column=5)
lbl21=Label(root,text="60",font=('Times New Roman',14,'bold')).grid(row=15,column=6)
et8=Entry(root,textvariable=h,font=('Times New Roman',14,'bold')).grid(row=15,column=7)

lbl22=Label(root,text="rice(full)",font=('Times New Roman',14,'bold')).grid(row=16,column=5)
lbl23=Label(root,text="120",font=('Times New Roman',14,'bold')).grid(row=16,column=6)
et9=Entry(root,textvariable=i,font=('Times New Roman',14,'bold')).grid(row=16,column=7)

lbl24=Label(root,text="hot and sour soup",font=('Times New Roman',14,'bold')).grid(row=17,column=5)
lbl25=Label(root,text="180",font=('Times New Roman',14,'bold')).grid(row=17,column=6)
et10=Entry(root,textvariable=j,font=('Times New Roman',14,'bold')).grid(row=17,column=7)

lbl26=Label(root,text="sweet corn soup",font=('Times New Roman',14,'bold')).grid(row=18,column=5)
lbl27=Label(root,text="170",font=('Times New Roman',14,'bold')).grid(row=18,column=6)
et11=Entry(root,textvariable=k,font=('Times New Roman',14,'bold')).grid(row=18,column=7)

lbl28=Label(root,text="tomato soup",font=('Times New Roman',14,'bold')).grid(row=19,column=5)
lbl29=Label(root,text="170",font=('Times New Roman',14,'bold')).grid(row=19,column=6)
et12=Entry(root,textvariable=l,font=('Times New Roman',14,'bold')).grid(row=19,column=7)

lbl30=Label(root,text="mushroom soup",font=('Times New Roman',14,'bold')).grid(row=20,column=5)
lbl31=Label(root,text="190",font=('Times New Roman',14,'bold')).grid(row=20,column=6)
et13=Entry(root,textvariable=m,font=('Times New Roman',14,'bold')).grid(row=20,column=7)

lbl32=Label(root,text="papad",font=('Times New Roman',14,'bold')).grid(row=21,column=5)
lbl33=Label(root,text="20",font=('Times New Roman',14,'bold')).grid(row=21,column=6)
et14=Entry(root,textvariable=n,font=('Times New Roman',14,'bold')).grid(row=21,column=7)

lbl34=Label(root,text="Masala papad",font=('Times New Roman',14,'bold')).grid(row=22,column=5)
lbl35=Label(root,text="40",font=('Times New Roman',14,'bold')).grid(row=22,column=6)
et15=Entry(root,textvariable=o,font=('Times New Roman',14,'bold')).grid(row=22,column=7)

lbl37=Label(root, font=('Times New Roman',14,'bold'), text="Subtotal").grid(row=24, column=5,pady=5)
et17= Entry(root,textvariable=st,font=('Times New Roman',14,'bold')).grid(row=24, column=7,pady=5)

lbl38= Label(root, font=('Times New Roman',14,'bold'), text="Tax").grid(row=25, column=5)
et18 = Entry(root, font=('Times New Roman',14,'bold'),textvariable=tax).grid(row=25,column=7)

lbl39= Label(root, font=('Times New Roman',14,'bold'), text="total quantities").grid(row=26, column=5)
et19= Entry(root, font=('Times New Roman',14,'bold'),textvariable=qty).grid(row=26,column=7)

lbl40=Label(root, font=('Times New Roman',14,'bold'), text="Service").grid(row=27, column=5)                                                                                                             
et20= Entry(root, font=('Times New Roman',14,'bold'),textvariable=service).grid(row=27, column=7)

lbl41 = Label(root, font=('Times New Roman',14,'bold'), text="Total").grid(row=28,column=5)                                                                                                         
et21= Entry(root, font=('Times New Roman',14,'bold'),textvariable=total).grid(row=28, column=7)

btn1=Button(root,text='GENERATE BILL',font=('Times New Roman',14,'bold'),command=bill,bg='yellow',fg='red').grid(row=29,column=4,pady=5)
btn2=Button(root,text='EXIT',font=('Times New Roman',14,'bold'),command=exit,bg='yellow',fg='red').grid(row=29,column=6,pady=5)
root.mainloop()


program 2: attendance systems
import mysql.connector as m
db=m.connect(host="localhost",user="root",passwd="Mahir@7314")
cur=db.cursor()
print("Cursor Created")
cur.execute("create database if not exists dylan")
cur.execute("use My_first_db")
print("Move in to database")
cur.execute("create table if not exists students1(grno int primary key, fname varchar(40), lname varchar(40), cls int, grade varchar(40), dob date, doj date,fees int NOT NULL)")
print("Table created")

def insert():

    grno=input('enter grno:')
    fname=input('enter first name:')
    lname=input('entrer last name:')
    cls=input('entrer class of student')
    grade=input('entrer section of the student:')
    dob=input('entrer the date of birth of the student(yyyy-mm-dd):')
    doj=input('entrer the date of joining the school(yyyy-mm-dd):')
    fees=input('enter the fees charged for that student:')
    a=("insert into students1(grno,fname,lname,cls,grade,dob,doj,fees) values(%s, %s, %s, %s, %s, %s, %s, %s)")
    cur.execute(a, (grno, fname, lname, cls, grade, dob, doj, fees))
    db.commit()
    print("Successful Insertion Done...")


def display():
    cur.execute("select * from students1")
    for i in cur:
        print(i)

def delete():
    grno = int(input('Enter grno to delete: '))
    sql = ("DELETE FROM students1 WHERE grno ='"+str(grno)+"' ")
    cur.execute(sql)
    db.commit()
    print("Deletion Done Successfully")

def edit():
    print('1.update name:')
    print('2.surname')
    print('3.section')
    print('4.fees')
    print('press any key for exit')
    ch=int(input("Enter : "))
    if ch==1:
        sid=int(input("Enter GRNO : "))
        nm=input("Enter New Name : ")
        cur.execute("update students1 set fname='"+nm+"' where grno='"+str(sid)+"' ")
        db.commit()
        print("Successful Update")
    elif ch==2:
        sid=int(input('enter GRNO:'))
        sn=input('enter the new surname:')
        cur.execute("update students1 set lname='"+sn+"' where grno='"+str(sid)+"' ")
        db.commit()
        print("/nSuccessful/n")
    elif ch==3:
        sid=int(input('enter GRNO:'))
        gr=input('enter the changed grade:')
        cur.execute("update students1 set grade='"+gr+"' where grno='"+str(sid)+"' ")
        db.commit()
        print("/nSuccessful/n")
    elif ch==4:
        sid=int(input('enter GRNO:'))
        fn=input('enter the updated fees:')
        cur.execute("update students1 set fees='"+fn+"' where grno='"+str(sid)+"' ")
        db.commit()
        print("/nSuccessful/n")
    elif c==5:
        exit(0)
while True:
    print("1. Insert a student data")
    print("2. Delete a student data")
    print("3. Show all students data")
    print("4. update the record of student")
    print("5. Exit")
    c=int(input('enter  what u want to see(1-5):'))
    if c==1:
        insert()
    elif c==2:
        delete()
    elif c==3:
        display()
    elif c==4:
       edit()
    elif c==5:
        exit(0)

program 3: libraryy systems
import mysql.connector as m
db=m.connect (host="localhost",user="root",passwd="Mahir@7314")
cur=db.cursor()
cur.execute("create database if not exists LIBRARY")
cur.execute("use LIBRARY")
cur.execute("create table if not exists book_data(bookid int primary key,bname varchar(100),bprice int,bauthor varchar(100), bpub varchar(100), qty int, bpub_date date)")
cur.execute("create table if not exists mem_data(mem_id int primary key,mem_name varchar(40), date_of_joinig date, validity date, ph_no int, city varchar(40))")
def bookdata():
    print('/n')
    print('1. insert data ')
    print('2. show data')
    print('3. update data')
    print('4. delete data')
    print('/n')
    ap=int(input('what do u want to do with book table(1-4):'))
    print('/n')
    if ap==1:
        bookid=input('enter book id:')
        bname=input('enter book name:')
        bprice=input('enter book price:')
        bauthor=input('enter author name of that book:')
        bpub=input('enter the publishing house name:')
        qty=input('enter the quantity of books available:')
        bpub_date=input('enter the date of publishing the book by the publisher:')
        a=("insert into students1(bookid,bname,bprice,bauthor,bpub,qty,bpub_date) values(%s, %s, %s, %s, %s, %s, %s)")
        cur.execute(a, (bookid,bname,bprice,bauthor,bpub,qty,bpub_date))
        db.commit()
        print('/n')
        print("Successful Insertion Done...")
    elif ap==2:
        print('/n')
        cur.execute("select * from book_data")
        for i in cur:
            print(i)
            print('/n')
        print('/n')
    elif ap==3:
        print('/n')
        print('1. changing book name:')
        print('2. changing price')
        print('3. changing date of publication(yyyy-dd-mm)')
        print('4. changing quantity of the books')
        print('/n')
        vr=int(input('enter your choice(1-4):'))
        print('/n')
        if vr==1:
             bookid=int(input("Enter bookid : "))
             nm=input("Enter New Name : ")
             cur.execute("update book_data set bname='"+nm+"' where bookid='"+str(bookid)+"' ")
             db.commit()
             print('/n')
             print("Successful Update")
             print('/n')
        elif vr==2:
            bookid=int(input("Enter bookid : "))
             bp=input("Enter New price: ")
             cur.execute("update book_data set bprice='"+bp+"' where bookid='"+str(bookid)+"' ")
             db.commit()
             print('/n')
             print("Successful Update")
             print('/n')
        
            
def memberdata():
    mem_id=input('enter member id:')
    mem_name=input('enter member name:')
    date_of_joining=input('enter date of joining:')
    validity=input('enter validity:')
    ph_no=input('enter phone number:')
    city=input('city of member:')
    a=("insert into students1(mem_id,mem_name,date_of_joining,validity,ph_no,city) values(%s, %s, %s, %s, %s, %s)")
    cur.execute(a, (mem_id,mem_name,date_of_joining,validity,ph_no,city))
    db.commit()
    print("Successful Insertion Done...")

while True:
    print('/n')
    print("1. book data")
    print("2. member data")
    print("3. Exit")
    print('/n')
    c=int(input('enter  what u want to see(1-3):'))
    print('/n')
    if c==1:
        print('/n')
        bookdata()
        print('/n')
    elif c==2:
        print('/n')
        memberdata()
        print('/n')
    elif c==3:
        exit(0)
