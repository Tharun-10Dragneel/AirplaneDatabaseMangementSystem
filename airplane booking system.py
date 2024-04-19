import mysql as scdef R_Homepage():
    print('*********************************')
    print("WELCOME TO INDIAN AIRLINES")
    print("********************************")
    print("1. ADD AEROPLANE DETAILS")
    print("2. UPDATE AEROPLANCE DETAILS")
    print("3. CANCEL AEROPLANE DETAILS")
    print("4. SEARCH AEROPLANE DETAILS")    
    print("5. TICKET BOOKING")
    print("6. CANCEL TICKET BOOKING")
    print("7. SEARCH BOOKING DETAILS")
    print("8. REPORT ")
    op=int(input("Enter your option:"))
    if op==1:
        Addplane()
    elif op==2:
        Updateplane()
    elif op==3:
        Removeplane ()
    elif op==4:
        Searchplane ()
    elif op==5:
        TicketBooking()
    elif op==6:
        SearchTicket()
    elif op==7:
        CancelBooking() 
    else:
        print("Invalid option")
        


#Definition for the Login () 
def Login():
    print("\n\n\n\n")
    print("***************************")
    print("WELCOME TO INDIAN AIRLINES")
    print("*****************************")
    user=input("Enter User Name:")
    pas=input("Enter password:")
    if user=='Adminplane' and pas=='1111':
        print("SUCCESSFUULY LOGGED!!!!!!")
        R_Homepage()
    else:
        print("INCORRECT CREDENTIALS")
        Login()

#Definition for Addplane() function
def Addplane():
    print("\n\n\n\n")
    print("***************************")
    print("WELCOME TO INDIAN AIRLINES")
    print("*****************************")
    print("ADD PLANE DETAILS")
    T_id=input("Enter Plane ID ")
    T_name=input("Enter Plane NAme:")
    T_startloc=input("Enter Starting Location:")
    T_endloc=input("Enter Ending location:")
    T_starttime=input("Enter starting time:")
    T_endtime=input("Enter ending time:")
    T_nooffirst=int(input("Enter no of first class seats:"))
    T_noofbusiness=int(input("Enter no of business seats"))
    T_noofeconomy=int(input("Enter no of economy class seat:"))
    T_pricefirst=int(input("Enter price of First class ticket:"))
    T_pricebuisness=int(input("Enter price of business class ticket:"))
    T_priceeconomy=int(input("Enter price of economy class ticket:"))
    conn=sc.connect(host="localhost",user="root",password="L290",database="plane12")
    mycursor=conn.cursor()
    query="insert into plane values(plane set starttime='{}',endtime='{}',Nooffirst={},noofbusiness={},noofeconomy={},pricefirst={},pricebuisness={},priceeconomy={} where: Tid='{}'".format(T_id,T_name,T_startloc,T_endloc,T_starttime,T_endtime,T_noofecofirst,T_noofbusinness,T_noofeconomy,T_pricefirst,T_pricebusiness,T_priceeconomy)
    mycursor.execute(query)
    conn.commit()
    print("SUCCESSFULLY ADD PLANE DETAILS !!!!!!")
    conn.close()
    

#DeDefinition of Updateplane() function
def Updateplane():
    print("\n\n\n\n")
    print("***************************")
    print("WELCOME TO PLANE RAILWAY")
    print("*****************************")
    print("UPDATE PLANE DETAILS")
    T_id=input("Enter Plane ID  to be updated ")
    T_starttime=input("Enter updated starting time:")
    T_endtime=input("Enter updated ending time:")
    T_nooffirst=int(input("Enter updated no of first class seats "))
    T_noofbuisness=int(input("Enter updated no of business class seats "))
    T_noofeconomy=int(input("Enter updated no of economy class seats"))
    T_pricefirst=int(input("Enter updated price of first class ticket"))
    T_pricebusiness=int(input("Enter updated price of business class ticket"))
    T_priceeconomy=int(input("Enter updated price of economy class ticket "))
    conn=sc.connect(host="localhost",user="root",password="L290",database="plane12")
    mycursor=conn.cursor()
    query="update plane set starttime='{}',endtime='{}',Nooffirst={},noofbusiness={},noofeconomy={},pricefirst={},pricebuisness={},priceeconomy={}"
    "where: Tid='{}'".format(T_starttime,T_endtime,T_noofac,T_noofsleeper,T_noofgeneral,T_priceac,T_pricesleeper,T_pricegeneral,T_id)
    mycursor.execute(query)
    conn.commit()
    print("SUCCESSFULLY UPDATED PLANE DETAILS !!!!!!")
    conn.close()

#DeDefinition for the Removeplane() function
def Removeplane():
    print("\n\n\n\n")
    print("***************************")
    print("WELCOME TO INDIAN AIRLINES")
    print("*****************************")
    print("REMOVE PLANE DETAILS")
    T_id=input("Enter Plane ID  to be removed  ")
    conn=sc.connect(host="localhost",user="root",password="L290",database="plane12")
    mycursor=conn.cursor()
    query="delete from plane where Tid='{}'".format(T_id)
    mycursor.execute(query)
    conn.commit()
    print("SUCCESSFULLY REMOVED PLANE DETAILS !!!!!!")
    conn.close()
    

#Definition for Search plane details.
def Searchplane():
    print("\n\n\n\n")
    print("***************************")
    print("WELCOME TO INDIAN AIRLINES")
    print("*****************************")
    print("SEARCH PLANES DETAILS")
    T_id=input("Enter Plane ID  to be Search   ")
    conn=sc.connect(host="localhost",user="root",password="L290",database="plane12")
    mycursor=conn.cursor()
    query="select * from plane where Tid='{}'".format(T_id)
    mycursor.execute(query)
    myrecord=mycursor.fetchall()
    for x in myrecord:
        print(x)
    conn.close()
    
#Definition for TicketBooking() function 
def TicketBooking():
    print("\n\n\n\n")
    print("***************************")
    print("WELCOME TO INDIAN AIRLINES")
    print("*****************************")
    print("TICKET BOOKING SECTION ")
    conn=sc.connect(host="localhost",user="root",password="L290",database="plane12")
    mycursor=conn.cursor()
    query="select * from train"
    mycursor.execute(query)
    myrecord=mycursor.fetchall()
    print("TID\t\tTname\t\tSTARTINGPOINT\t\tENDLOC\t\tSTARTTIME\t\tENDTIME\t\tNOOFfirst\t\tNOOFbuisness\t\tNOOFeconomy\t\tPRICEfirst\t\
    tPRICEbusiness\t\tPRICEeconomy\t\t\n")
    for x in myrecord:
        print(x[0],'\t\t',x[1],"\t\t",x[2],"\t\t",x[3],"\t\t",x[4],"\t\t",x[5],"\t\t",x[6],"\t\t",x[7],"\t\t",x[8],"\t\t",x[9],"\t\t",x[10],
              "\t\t",x[11],"\n")
    conn.close()
    Tid=input("Enter ID of the Plane you are Booking")
    tname=input("Enter name of the plane")
    adharnouser=int(input("Enter your Ahdar No"))
    name=input("Enter your name")
    age=int(input("Enter your age"))
    typeticket=input("Enter type of Ticket(Firstclass/Businessclass/Economyclass)")
    startloc=input("Starting location")
    endloc=input("Enter Destination location")
    conn=sc.connect(host="localhost",user="root",password="L290",database="plane12")
    fare=0
    mycursor=conn.cursor()
    query="select *  from plane where Tid='{}'".format(Tid)
    mycursor.execute(query)
    myrecord=mycursor.fetchall()
    for x in myrecord:
        if typeticket=="FIRST CLASS":
            fare=x[9]
            n=x[6]-1
            query2="update train set nooffirst={} where Tid='{}'".format(n,Tid)
        elif typeticket=="BUSINESS CLASS":
            fare=x[10]
            n=x[7]-1
            query2="update train set noofbusiness={} where Tid='{}'".format(n,Tid)
        elif typeticket=="ECONOMY CLASS":
            fare=x[11]
            n=x[8]-1
            query2="update train set noofeconomy={} where Tid='{}'".format(n,Tid)
            mycursor.execute(query2)
            conn.commit()
            conn.close()
            if age>=60 or age<=10:
                fare=fare-fare*50/100
            else:
                fare=fare
            conn=sc.connect(host="localhost",user="root",password="L290",database="plane12")
            mycursor=conn.cursor()
            query="insert into planebooking values('{}','{}',{},'{}',{},'{}','{}','{}',{})".format(Tid,tname,adharnouser,name,age,typeticket,s
            tartloc,endloc,fare)
            mycursor.execute(query)
            conn.commit()
            print("SUCCESSFULLY DONE TICKET BOOKING !!!!!!")
            conn.close()
    
# Definition for SearchBooking() function
def SearchBooking():
    print("\n\n\n\n")
    print("***************************")
    print("WELCOME TO INDIAN AIRLINES")
    print("*****************************")
    print("TICKET BOOKING SECTION ")
    ano=int(input("Enter your adhar number for checking"))
    conn=sc.connect(host="localhost",user="root",password="L290",database="plane12")
    mycursor=conn.cursor()
    query="select *  from trainbooking where adharno_user={}".format(ano)
    mycursor.execute(query)
    myrecord=mycursor.fetchall()
    for x in myrecord:
        print(x)
    else:
        print("No Booking in this Adhar No")
    conn.close() 
    
    
#Definition for CancelTicket() function
def CancelTicket():
    print("\n\n\n\n")
    print("***************************")
    print("WELCOME TO INDIAN AIRLINES")
    print("*****************************")
    print("TICKET BOOKING SECTION ")
    ano=int(input("Enter your adhar number for cancellation"))
    conn=sc.connect(host="localhost",user="root",password="L290",database="plane12")
    mycursor=conn.cursor()
    query1="select * from planebooking where adharno_user={}".format(ano)
    mycursor.execute(query1)
    myrecord=mycursor.fetchall()
    for x in myrecord:
        tid=x[0]
        tickettype=x[5]
    query3="select * from plane where Tid='{}'".format(tid) 
    mycursor.execute(query3)
    myrecord2=mycursor.fetchall()
    for x in myrecord2:
        if tickettype=="First Class":
            acno=x[6]+1
            query4="update plane set nooffirst={} where Tid='{}'".format(fino,tid)
        elif tickettype=="Business Class":
            slno=x[7]+1
            query4="update train set noofbusiness={} where Tid='{}'".format(buno,tid)
        elif tickettype=="Economy Class":
            gno=x[8]+1
            query4="update plane set noofeconomy={} where Tid='{}'".format(ecno,tid)        
    query="delete from planebooking where adharno_user={}".format(ano)
    mycursor.execute(query)
    conn.commit()
    mycursor.execute(query4)
    conn.commit()
    conn.close()     
# Definition of Report() function
def  Report():
    print("\n\n\n\n")
    print("***************************")
    print("WELCOME TO INDIAN AIRLINES")
    print("*****************************")
    print("TICKET BOOKING SECTION ")
    print("Different Types of Reports are")
    print("1. Report based on Type of seat and no of seats avilable in each type")
    print("2. Report Based on price of each Type of seat ")
    print("3. Report based on type of ticket booking ")
    op=int(input("Enter your option:"))
    if op==1:
        print("\n\n\n\n")
        print("***************************")
        print("WELCOME TO INDIAN AIRLINES")
        print("*****************************")
        print("TICKET BOOKING SECTION ")
        tid=input("Enter plane id:")
        query="select * from plane where tid='{}'".format(tid)
        conn=sc.connect(host="localhost",user="root",password="L290",database="plane12")
        mycursor=conn.cursor()
        mycursor.execute(query)
        myrecord=mycursor.fetchall()
        x=["First Class","Buisness Class","Economy Class"]
        y=[]
        y1=0
        y2=0
        y3=0
        for i in myrecord:
            y1=i[6]
            y2=i[7]
            y3=i[8]
        y.append(y1)
        y.append(y2)
        y.append(y3)
        plt.bar(x,y)
    elif op==2:
        print("\n\n\n\n")
        print("***************************")
        print("WELCOME TO INDIAN AIRLINES")
        print("*****************************")
        print("TICKET BOOKING SECTION ")
        tid=input("Enter plane id:")
        query="select * from plane where tid='{}'".format(tid)
        conn=sc.connect(host="localhost",user="root",password="L290",database="plane12")
        mycursor=conn.cursor()
        mycursor.execute(query)
        myrecord=mycursor.fetchall()
        x=["First Class","Business Class","Economy Class"]
        y=[]
        y1=0
        y2=0
        y3=0
        for i in myrecord:
            y1=i[9]
            y2=i[10]
            y3=i[11]
        y.append(y1)
        y.append(y2)
        y.append(y3)
        plt.bar(x,y)
    elif op==3:
        print("\n\n\n\n")
        print("***************************")
        print("WELCOME TO INDIAN AIRLINES")
        print("*****************************")
        print("TICKET BOOKING SECTION ")
        tid=input("Enter plane id:")
        query="select typeofseat,count(*) from Planebooking group by typeofseat"
        conn=sc.connect(host="localhost",user="root",password="L290",database="plane12")
        mycursor=conn.cursor()
        mycursor.execute(query)
        myrecord=mycursor.fetchall()
        x=[]
        y=[]
        for i in myrecord:
            x.append(i[0])
            y.append(i[1])      
        plt.bar(x,y,width=0.5)
        ply.xlabel("type of seat")
        plt.ylabel("no of seats booked on each type")   
     
    
#Calling main function
Login()
R_Homepage()     

   
