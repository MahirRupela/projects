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
