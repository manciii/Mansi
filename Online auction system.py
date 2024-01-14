import mysql.connector
con=mysql.connector.connect(host='localhost',password='@mansi@',user='root',database='auction')
mycursor=con.cursor()
'''query='create database auction;'
mycursor.execute(query)
query='use auction;'
mycursor.execute(query)
query='create table products(item_no integer primary key, item_name varchar(50), item_description varchar(50), reserve_price integer);'
mycursor.execute(query)
query='create table bidder(id integer primary key, username varchar(50), item_name varchar(50), bid integer, item_no integer);'
mycursor.execute(query)
query='create table registrations(ids integer primary key, names varchar(50));'
mycursor.execute(query)'''

def registration():
    global names,id
    names=input("username")
    id=int(input("create user id"))
    print("important note: remember your id for next use")
    query="insert into registrations values({},'{}')".format(id ,names)
    mycursor.execute(query)
    con.commit()
    print("you have successfully registered")
    return

def bid(id,username):
    global mycursor
    item_name=input("enter name of the product")
    item_no=int(input("enter item no of the product"))
    bid=int(input("enter your bid price"))
    query="insert into bidder values({},'{}','{}',{},{})".format(id,username,item_name,bid,item_no)
    mycursor.execute(query)
    con.commit()
    print("thanks! for bidding")
    return

def max_bid():
    global mycursor
    ino=98
    #input("enter the product no whose max bid you want to see")
    query="select max(bid),username from(select * row_number() order by bid desc rn from bidder)x where rn=1 and item_no= "+ str(ino)
    mycursor.execute(query)
    myproducts=mycursor.fetchone()
    print(myproducts)
    #query="select max(bid),username from(select * row_number() order by bid desc rn from bidder)x where rn=1"
    print("till now he has bid the highest price")
    c=mycursor.rowcount
    if c==-1:
        print("nothing to be displayed")
    return

def display_all_bidders():
    global mycursor
    query="select*from bidder"
    mycursor.execute(query)
    myproducts=mycursor.fetchall()
    for i in myproducts:
        print(i)
    return

def display_users():
    global mycursor
    query="select*from registrations"
    mycursor.execute(query)
    myproducts=mycursor.fetchall()
    for i in myproducts:
        print(i)
    return

def add_prod():
    global mycursor
    item_no=int(input("enter product id"))
    item_name=input("enter product name")
    item_description=input("enter product description")
    reserve_price=int(input("enter reserve price for your product"))
    query="insert into products values({},'{}','{}',{})".format(item_no,item_name,item_description,reserve_price)
    mycursor.execute(query)
    con.commit()
    print("data added successfully")
    return

def display_selected_prod():
    global mycursor
    ino=int(input("enter product id whose information is to be display"))
    query="select*from products where item_no= "+str(ino)
    mycursor.execute(query)
    myproducts=mycursor.fetchone()
    print("\n information of product whose id is",ino)
    print(myproducts)
    c=mycursor.rowcount
    if c==-1:
        print("nothing to be displayed")
    return

def display_all_prod():
    global mycursor
    query="select*from products"
    mycursor.execute(query)
    myproducts=mycursor.fetchall()
    for i in myproducts:
        print(i)
    return

def del_prod():
    global mycursor
    ino=int(input("enter product id which you have to delete"))
    query="delete from products where item_no= "+ str(ino)
    mycursor.execute(query)
    con.commit()
    c=mycursor.rowcount
    if c>0:
        print("\nproduct is deleted whose id is",ino)
    else:
        print("product with product id",ino,"not found")
    return
def al_choices():
    while True:
        print('\n\n\n')
        print('***'*50)
        print('\t\t\t\t\t\t\t\tMAIN MENU')
        print('***'*50)
        print("\t\t\t\t\t\t\t\t1.Show All Products")
        print("\t\t\t\t\t\t\t\t2.Add Products")
        print("\t\t\t\t\t\t\t\t3.Delete Products")
        print("\t\t\t\t\t\t\t\t4.Show Selected Products")
        print("\t\t\t\t\t\t\t\t5.Bid")
        print("\t\t\t\t\t\t\t\t6.Show Bidders")
        print("\t\t\t\t\t\t\t\t7.Winner")
        print("\t\t\t\t\t\t\t\t8.Show All Users")
        print("\t\t\t\t\t\t\t\t9.To Exit")
        print("enter choice",end='')


        choice=int(input())
        if choice==1:
            display_all_prod()
        elif choice==2:
            add_prod()
        elif choice==3:
            del_prod()
        elif choice==4:
            display_selected_prod()
        elif choice==5:
            bid(id,names)
        elif choice==6:
            display_all_bidders()
        elif choice==7:
            max_bid()
        elif choice==8:
            display_users()
        elif choice==9:
            break
        else:
            print("invalid choice........please enter write choice i.e.1,2,3,4,5")
        input()
print('\t\t\t\t\t\t\t\tA.login')
print('\t\t\t\t\t\t\t\tB.register')
choose=input('enter your choice')
if choose=='b':
      registration()
elif choose=='a':
    a=int(input('enter id'))
    username=input("enter you registered name")
    names=username
    id=a
    query="select * from registrations where ids= " + str(a)
    mycursor.execute(query)
    mynames=mycursor.fetchone()
    print(mynames)
    print("if above is your username and id print Y otherwise print N")
    c=input('enter choice')
    if c=='Y':
        al_choices()
    else:
        registration()
else:
    print('choose only A or B')
al_choices()









