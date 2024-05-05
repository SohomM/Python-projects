print("                  -> WELCOME TO RYNA CLOTH SHOP <-")
print("----------------------CLOTH MANAGEMENT SYSTEM-----------------------")
from datetime import datetime
now_method = datetime.now()
currentTime = now_method.strftime("%H:%M:%S")
print(" Time =",currentTime,"         Address: 26/A NORTH STREET,KOLKATA")
print("----------------------------LOGIN FIRST-----------------------------")
print("NOTE: login id is 4-digit code")
a=input("LOGIN WITH EMPLOYEE-ID : ")
print("CONNECTED")
print("--------------------------------------------------------------------")
print("ALWAYS MAINTAIN NEW DATA INPUT ORDER AS ASKED")
print("**************************************************")
print("1-EMPLOYEES  2-STOCK  3-CUSTOMER INFO  4-LOGOUT")
b=int(input("Enter 1/2/3/4 to continue : "))
if b==4:
    print("--*THANK YOU*--")
elif b==3:
    print("customer info is auto-saved. Mail to cloth@ryna.com for editing.")
    print("---------------------------------------------------------------")
    custo=open("CUST.txt","r")
    str=custo.read()
    print(str)
    custo.close()
elif b==2:
    st=open("STOCK.txt","r")
    str=st.read()
    print(str)
    st.close()
    z=int(input("1.ADD  2.ORDER (enter 1/2 to continue): "))
    if z==1:
       st=open("stock.txt","a")
       take=input("how many data to add ? ")
       for i in take:
            name=input("ITEM_NO - NAME - PRICE : ")
            st.write(name)
            st.write('\n')
       st.close()
       print("--------DONE--------")
    else:
        print("Visit website to place order .")
else:
    empatten=open("empattend.txt","r")
    str=empatten.read()
    print(str)
    empatten.close()
    print("--------------------------------------------------------------")
    c=int(input("1.ADD  2.REMOVE  3.EXIT (enter 1/2/3 : "))
    if c==3:
        print("--**EXITING**--")
    elif c==2:
        ask=input("Enter EMPID to delete : ")
        try:
            with open("EMPATTEND.txt","r+") as fw:
                for line in str:
                    if line.strip('\n') != ask:
                        fw.write(line)
            print(ask," is deleted.")
        except:
            print("operation failed! ")
    else :
        emp=open("empattend.txt","a")
        take=input("how many data to add ? ")
        for i in take:
            name=input("EMPID - NAME - DEPT : ")
            emp.write(name)
            emp.write('\n')
        emp.close()
        print("------DONE------")
print("HISTORY SAVED")        
