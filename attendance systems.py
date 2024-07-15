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
