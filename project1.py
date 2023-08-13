import mysql.connector as sqltor

mycon=sqltor.connect(host='localhost',username='root',password='Tab04082003@',database='project1')
if mycon.is_connected():
    print("successfully connected to the database")
else:
    print("Error connecting to MySQL Database")
cur=mycon.cursor()

choice=None
ch='Y'
while choice!=7 and ch=='Y':
    print("---------MENU--------")
    print("1.Insert A Customer Record")
    print("2.Display Customer and Booking Details")
    print("3.Search Customer")
    print("4.Update customer details")
    print("5.Delete A Record")
    print("6.Exit")
    choice=int(input("Enter your choice:"))
    a='Y'
    if choice==1:
        while a=='Y':
            mycon=sqltor.connect(host='localhost',username='root',password='Tab04082003@',database='project1')
            if mycon.is_connected():
                print("successfully connected to the database")
            else:
                print("Error connecting to MySQL Database")
            cur=mycon.cursor()
            cid=int(input("Enter cid : "))
            cname=input("Enter Customer Name :")
            phn=input("Enter Phone No. :")
            email=input("Enter Email :")
            age=int(input("Enter Age :"))
            # Add booking details also
            Room_No=int(input("Enter Room No. :"))
            Room_Type=input("Enter Room Type :")
            check_in=input("Enter Check-in Dtae :")
            check_out=input("Enter check-out date :")
            cost=input("Enter cost :")
            print("Want to add more records:(Y/N) ")
            a=input("Enter your choice : ")
            st= "insert into customer(cid,cname,phn,email,age) values({},'{}','{}','{}',{})".format(cid,cname,phn,email,age)
            # st2="insert intp booking-details(cid,Room_No,Room_Type,check_in,check_out,cost) values({},{},'{}','{}','{}',{})".format(cid,Room_No,Room_Type,check_in,check_out,cost)
            cur.execute(st)
            # cur.execute(st2)
            mycon.commit()
    if choice==2:
        mycon=sqltor.connect(host='localhost',username='root',password='Tab04082003@',database='project1')
        if mycon.is_connected():
            print("successfully connected to the database")
        else:
            print("Error connecting to MySQL Database")
        cur=mycon.cursor()
        cur.execute("Select * from customer,booking_details where customer.cid=booking_details.cid")
        data=cur.fetchall()
        for row in data:
            print(row)
    if choice==3:
        mycon=sqltor.connect(host='localhost',username='root',password='Tab04082003@',database='project1')
        if mycon.is_connected():
            print("successfully connected to the database")
        else:
            print("Error connecting to MySQL Database")
        cur=mycon.cursor()
        search=int(input("Enter cid for Customer to be searched :"))
        st="select * from customer where cid={}".format(search)
        cur.execute(st)
        data=cur.fetchall()
        print(data)
        mycon.commit()      
    if choice==4:
        mycon=sqltor.connect(host='localhost',username='root',password='Tab04082003@',database='project1')
        if mycon.is_connected():
            print("successfully connected to the database")
        else:
            print("Error connecting to MySQL Database")
        cur=mycon.cursor()
        cid=int(input("Enter customer id to be updated :"))
        
        value=input("Enter value to be updated :")
        updated=input("Enter updated value :")
        # st="update customer set {value}={} where cid={}".format(updated,cid)
        st = "UPDATE customer SET {} = {} WHERE cid = {}".format(value, updated, cid)
        cur.execute(st)
        data=cur.fetchall()
        print(data)
    if choice==5:
        mycon=sqltor.connect(host='localhost',username='root',password='Tab04082003@',database='project1')
        if mycon.is_connected():
            print("successfully connected to the database")
        else:
            print("Error connecting to MySQL Database")
        cur=mycon.cursor()
        cid=int(input("Enter customer whose information needs to be deleted :"))
        st="delete from customer where cid={c}".format(c=cid)
        cur.execute(st)
        cur.execute("select * from customer")
        data=cur.fetchall()
        for row in data:
            print(row)
    if choice==6:
        print("Have A Nice Day Ahead")
    ch=input("Want to conyinue(Y/N)? :")
