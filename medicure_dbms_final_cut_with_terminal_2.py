import mysql.connector
import sys
import os
import time


x=mysql.connector.connect(host='localhost',user='root',passwd='karthik_rajeev_25')
y=x.cursor()
y.execute('drop database medicuredbms')
y.execute('create database medicuredbms')
y.execute('set autocommit=1')
y.execute("use medicuredbms")
y.execute('create table Doctor_Details(Doc_id int(5) primary key,Name varchar(25),Dept varchar(25),Address varchar(50),Phno char(10))')
y.execute('create table Patient_Details(Patient_id int(5) primary key,Name varchar(25),Age int(3),Gender char(2),Address varchar(100),\
Phno char(10),RoomNumber char(4),Doctorname varchar(25),Dept varchar(25),Doc_id int (5),FOREIGN KEY (Doc_id) REFERENCES Doctor_Details(Doc_id))')

def main():
    t=1
    while True:
        print("+-------------------------------------------------------------------+")
        print("|                                                                   |")
        print("|          Welcome to Medicure Database Management System           |")
        print("|                                                                   |")
        print("+-------------------------------------------------------------------+")
        print("+-------------------------------------------------------------------+")
        print("|                      Enter 1 for Admin Mode                       |")
        print("+-------------------------------------------------------------------+")
        print("|                      Enter 2 for User Mode                        |")
        print("+-------------------------------------------------------------------+")
        print("|                      Enter 3 to Exit                              |")
        print("+-------------------------------------------------------------------+")
        Mode = input("Enter your mode : ")
        if Mode == "1" : #Admin mode
            Password = input("Please enter your password : ")
            while True :
                if Password == "1234" :
                    os.system('cls')
                    print("+----------------------------------------------------------------+")
                    print("|                     Welcome to admin mode                      |")
                    print("+----------------------------------------------------------------+")
                    print("|                    To manage patients      Enter 1             |")
                    print("|                    To manage doctors       Enter 2             |")
                    print("|                    To switch modes         Enter S             |")
                    print("|                    To open MYSQL DIRECT    Enter 3             |")
                    print("+----------------------------------------------------------------+")
                    AdminOpt = input ("Enter your choice : ")
                    AdminOpt = AdminOpt.upper()
                    os.system('cls')
                    if AdminOpt == "1" : #Admin mode --> Patient Management
                        while True:
                            print("+-------------------------------------------------------------------------------+")
                            print("|                To add new patient                          Enter 1            |")
                            print("|                To display patient details                  Enter 2            |")
                            print("|                To delete patient data                      Enter 3            |")
                            print("|                To edit patient data                        Enter 4            |")
                            print("|                To view patient table                       Enter 5            |")
                            print("|                To view list of patients in particular dept Enter 6            |")
                            print("|                To go Back                                  Enter B            |")
                            print("+-------------------------------------------------------------------------------+")
                            AChoice = input ("Enter your choice : ")
                            AChoice = AChoice.upper()
                            os.system('cls')
                            if AChoice == "1" :   #Admin mode-->Patient Management-->Add patient
                                addpatient()
                                CONTINUE()
                            elif AChoice == "2" : #Admin mode-->Patient Management-->View patient details
                                viewpatient()
                                CONTINUE()
                            elif AChoice == "3" : #Admin mode -->Patient Management --> Delete patient data
                                deletepatient()
                                CONTINUE()
                            elif AChoice == "4" : #Admin mode --> Patient Management --> Edit patient data
                                editpatient()
                            elif AChoice =='5':   #Admin mode -->Patient Management-->View patient table
                                viewfullpattable()
                                CONTINUE()
                            elif AChoice=='6':    #Admin mode -->Patient Management-->View list of patients in a given department
                                deptpatlst()
                                CONTINUE()
                            elif AChoice=='B':    #Admin mode-->Patient Management-->back
                                break
                            else:
                                print('please enter correct option')
                    
                    elif AdminOpt == "2" : #Admin mode --> Doctors Management
                        while True:
                            print("+---------------------------------------------------------------------------------+")
                            print("|                     To add new doctor                                  Enter 1  |")
                            print("|                     To display doctor                                  Enter 2  |")
                            print("|                     To delete doctor data                              Enter 3  |")
                            print("|                     To edit doctor data                                Enter 4  |")
                            print("|                     To view full doctor table                          Enter 5  |")
                            print("|                     To view list of patients treated by doc            Enter 6  |")
                            print("|                     To view list of doctors working in particular dept Enter 7  |")
                            print("|                     To go back                                         Enter B  |")
                            print("+---------------------------------------------------------------------------------+")
                            AChoice = input ("Enter your choice : ")
                            AChoice = AChoice.upper()
                            os.system('cls')
                            if AChoice == "1" : #Admin mode --> Doctors Management --> Enter new doctor data
                                adddoc()
                                CONTINUE()
                            elif AChoice == "2" : #Admin mode --> Doctors Management --> Display doctor data
                                dispdoc()
                                CONTINUE()
                            elif AChoice == "3" : #Admin mode --> Doctors Management --> Delete doctor data
                                deldoc()
                                CONTINUE()
                            elif AChoice == "4" : #Admin mode --> Doctors Management --> Edit Doctor data
                                editdoc()
                            elif AChoice =="5":#Admin_mode--> Doctors Management--> View full Doctor Table 
                                viewfulldoctable()
                                CONTINUE()
                            elif AChoice=="6":#Admin_mode--> Doctors Management--> View list of patients treated by Doctor 
                                docpatlst()
                                CONTINUE()
                            elif AChoice=="7":#Admin_mode--> Doctors Management--> View list of doctors in a particular department
                                deptdoclst()
                                CONTINUE()
                            elif AChoice == "B":#Admin_mode--> Doctors Management--> back
                                break
                            else:
                                print('please enter correct option')
                    elif AdminOpt =='3':#Admin_mode-->MYSQL DIRECT
                        os.system('cls')
                        MYSql()
                    elif AdminOpt =='S':#Admin_mode-->Switch Modes
                        os.system('cls')
                        main()
                    else:
                        print('please enter correct option')
                else :#incorrect password
                    while t< 3 :
                        Password = input("Password incorrect, please try again : ")
                        t+= 1
                        if Password=="1234":
                            t-=1
                            break
                    if t==3:
                        print("You have been locked out of the system.....")
                        time.sleep(5)
                        sys.exit()
                   
        elif Mode == "2" : #User mode
            os.system('cls')
            while True:
                print("+---------------------------------------------------------------+")
                print("|                     Welcome to user mode                      |")
                print("+---------------------------------------------------------------+")
                print("+---------------------------------------------------------------+")
                print("|             To view hospital's departments           Enter 1  |")
                print("|             To view hospital's doctors               Enter 2  |")
                print("|             To view patient's details                Enter 3  |")
                print("|             To switch modes                          Enter S  |")
                print("+---------------------------------------------------------------+")
                UOpt = input("Enter your choice : ")
                UOpt = UOpt.upper()
                os.system('cls')
                if   UOpt == "1" : #User mode --> view hospital's departments
                    dispdepuser()
                    CONTINUE()
                elif UOpt == "2" : #User mode --> view hospital's Doctors
                    dispdocuser()
                    CONTINUE()
                elif UOpt == "3" : #User mode --> view patient's details
                    viewpatient()
                    CONTINUE()
                elif UOpt == "S" : #Back
                    os.system('cls')
                    main()
                else :
                    print("Please Enter a correct choice")
        elif Mode=="3":
            sys.exit()
            
        else :
            print("Please choice just 1 or 2")


#function definitions
        
def addpatient():#funtion to add patient
    Patient_id=int(input("Enter patient ID                        : "))
    DoctorName    =input("Enter name of doctor following the case : ")
    Name          =input("Enter patient name                      : ")
    Age           =input("Enter patient age                       : ")
    Gender        =input("Enter patient gender                    : ")
    Address       =input("Enter patient address                   : ")
    Phno          =input("Enter patient phone number              : ")
    RoomNumber    =input("Enter patient room number               : ")
    Department    =input("Enter the department                    :")
    Doc_id   = int(input("Enter the doctor id                     : "))
    y.execute("insert into patient_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Patient_id,Name,Age,Gender,Address,\
    Phno,RoomNumber,DoctorName,Department,Doc_id ))
    print("----------------------Patient added successfully----------------------")


def viewpatient():#funtion to view patient details
    Patient_id= int(input("Enter patient ID : "))
    y.execute("select * from patient_details where Patient_id=(%s)",(Patient_id,)) 
    z=y.fetchall()
    for i in z:
        print("\npatient name                         : ",i[1])
        print("patient age                          : ",i[2])
        print("patient gender                       : ",i[3])
        print("patient address                      : ",i[4])
        print("patient phone number                 : ",i[5])
        print("patient room number                  : ",i[6])
        print("Patient's department                 : ",i[8])
        print("patient is followed by doctor        : ",i[7])
    if z==[]:
        print("no record found")

        
def deletepatient():#funtion to delete patient
    while True:
        Patient_id = int(input("Enter patient ID : "))
        y.execute("select * from patient_details where patient_id=(%s)",(patient_id,)) 
        z=y.fetchall()
        if z==[]:
            print('please enter correct id')
            continue
        else:
            y.execute("delete from patient_details where Patient_id=%s",(Patient_id,))
            print("----------------------Patient data deleted successfully----------------------")
            break
def editpatdep(Patient_id):#funtion to edit patient department
    Department=input("Enter correct department : ")
    y.execute("update patient_details set Department =%s where Patient_id =%s",(Department,Patient_id))
    print("----------------------Patient Department edited successfully----------------------")

def editpatdoc(Patient_id):#funtion to edit doctor following patient
    DoctorName=input("enter the correct doctors name : ")
    y.execute("update patient_details set DoctorName =%s where Patient_id =%s",(DoctorName,Patient_id))
    print("----------------------Doctor follouing case edited successfully----------------------")

def editpatname(Patient_id):#funtion to edit patient name
    Name=input("enter the correct patient's name : ")
    y.execute("update patient_details set Name =%s where Patient_id =%s",(Name,Patient_id))
    print("----------------------Patient name edited successfully----------------------")

def editpatage(Patient_id):#funtion to edit patient age
    Age=int(input("enter the correct patient's age : "))
    y.execute("update patient_details set Age =%s where Patient_id =%s",(Age,Patient_id))
    print("----------------------Patient age edited successfully----------------------")

def editpatgender(Patient_id):#function to edit patient gender
    Gender=input("enter the correct patient's gender : ")
    y.execute("update patient_details set Gender =%s where Patient_id =%s",(Gender,Patient_id))
    print("----------------------Patient address gender successfully----------------------")

def editpataddress(Patient_id):#funtion to edit patient address
    Address=input("enter the correct patient's address : ")
    y.execute("update patient_details set Address =%s where Patient_id =%s",(Address,Patient_id))
    print("----------------------Patient address edited successfully----------------------")

def editpatroom(Patient_id):#funtion to edit patient room no
     RoomNumber =int(input("enter the correct patient's roomno : "))
     y.execute("update patient_details set RoomNumber =%s where Patient_id =%s",(RoomNumber,Patient_id))
     print("----------------------Patient RoomNumber edited successfully----------------------")

def editphno(Patient_id):
    Phno=int(input("enter the correct patient's phone no. : "))#function to edit patient phone no
    y.execute("update patient_details set Phno =%s where Patient_id =%s",(Phno,Patient_id))
    print("----------------------Patient phoneno edited successfully----------------------")

def editdocid(Patient_id):
    Doc_id = int(input("enter the correct doctor's id : "))#function to edit doc id
    y.execute("update patient_details set Doc_id =%s where Patient_id =%s",(Doc_id,Patient_id))
    print("----------------------Doctor id edited successfully----------------------")

def editpatient():#funtion to edit patient
    while True :
        print("-----------------------------------------")
        print("To Edit patient Department      Enter 1 :")
        print("To Edit Doctor following case   Enter 2 :")
        print("To Edit patient Name            Enter 3 :")
        print("To Edit patient Age             Enter 4 :")
        print("To Edit patient Gender          Enter 5 :")
        print("To Edit patient Address         Enter 6 :")
        print("To Edit patient RoomNumber      Enter 7 :")
        print("To Edit patient phoneno         Enter 8 :")
        print("To Edit doctor's id             Enter 9 :")
        print("To be Back                      Enter B :")
        print("-----------------------------------------")
        Admin_choice = input("Enter your choice : ")
        Admin_choice = Admin_choice.upper()
        while True:
            if Admin_choice == "1" :
                editpatdep(Patient_id)
                CONTINUE()
                
            elif Admin_choice == "2" :
                editdoc(Patient_id)
                CONTINUE()
                    
            elif Admin_choice == "3" :
                editpatname(Patient_id)
                CONTINUE()
                    
            elif Admin_choice == "4" :
                editpatage(Patient_id)
                CONTINUE()
                    
            elif Admin_choice == "5" :
                editpatgender(Patient_id)
                CONTINUE()
                
            elif Admin_choice == "6" :
                editpataddress(Patient_id)
                CONTINUE()
                    
            elif Admin_choice == "7" :
                editpatroom(Patient_id)
                CONTINUE()
                    
            elif Admin_choice == "8" :
                editphno(Patient_id)
                CONTINUE()
                
            elif Admin_choice =='9':
                editdocid(Patient_id)
                CONTINUE()
                    
            elif Admin_choice == "B" :
                CONTINUE()
                break
            else :
                Achoice=int(input("Please Enter a correct choice"))


def viewfullpattable():#function to view full patient table
    y.execute('select * from Patient_Details')
    z=y.fetchall()
    for i in z:
        print('\n\n')
        l=len(i)
        for j in range(l):
            print(i[j],end='\t')
        

def adddoc():#funtion to add doctor
    Doc_id= int(input("Enter Doctor id                                      : "))
    Name=       input("Enter name of doctor                                 : ")
    Dept      = input("Enter Dept name                                      : ")
    Address    =input("Enter doctor's address                               : ")
    Phno    =   input("Enter phone number                                   : ")
    y.execute("insert into doctor_details values(%s,%s,%s,%s,%s)",(Doc_id,Name ,Dept ,Address ,Phno))
    print("----------------------Doctor added successfully----------------------")

def dispdoc():#funtion to disp doctor details
    Doc_id= int(input("Enter doctor ID : "))
    y.execute("select * from doctor_details where Doc_id=(%s)",(Doc_id,)) 
    z=y.fetchall()
    for i in z:
        print("\nDoctor  name                         : ",i[1])
        print("Doctor's Field                       : ",i[2])
        print("Doctor's address                     : ",i[3])
        print("Doctor's phone number                : ",i[4])
    if z==[]:
        print('please enter correct id')

def deldoc():#funtion to delete doctor
    while True:
        Doc_id = int(input("Enter doctor ID : "))
        y.execute("select * from doctor_details where Doc_id=(%s)",(Doc_id,)) 
        z=y.fetchall()
        if z==[]:
            print('please enter correct id')
            continue
        else:
            y.execute("delete from doctor_details where Doc_id=%s",(Doc_id,))
            print("----------------------Doctor data deleted successfully----------------------")
            break
def editdocdep():#function to edit doctor dep
    while True:
        Doc_id=int(input("Enter the doctor's id"))
        y.execute("select * from doctor_details where Doc_id=(%s)",(Doc_id,)) 
        z=y.fetchall()
        if z==[]:
            print('please enter correct id')
            continue
        else:
            Dept=input("Enter the correct department : ")
            y.execute("update doctor_details set Dept =%s where Doc_id =%s",(Dept,Doc_id))
            print("----------------------Doctor's department edited successfully----------------------/")
            break
def editdocname():#funtion to edit doctor name
    while True:
        Doc_id=int(input("Enter the doctor's id"))
        y.execute("select * from doctor_details where Doc_id=(%s)",(Doc_id,)) 
        z=y.fetchall()
        if z==[]:
            print('please enter correct id')
            continue
        else:
            Name=input("Enter the correct name : ")
            y.execute("update doctor_details set Name =%s where Doc_id =%s",(Name,Doc_id))
            print("----------------------Doctor's name edited successfully----------------------")
            break
def editdocaddress():#funtion to edit doctor address
    while True:
        Doc_id=int(input("Enter the doctor's id"))
        y.execute("select * from doctor_details where Doc_id=(%s)",(Doc_id,)) 
        z=y.fetchall()
        if z==[]:
            print('please enter correct id')
            continue
        else:
            Address=input("Enter the correct address : ")
            y.execute("update doctor_details set Address =%s where Doc_id =%s",(Address,Doc_id))
            print("----------------------Doctor's address edited successfully----------------------")
            break
def editdocphone():#funtion to edit doctor phone
    while True:
        Doc_id=int(input("Enter the doctor's id"))
        y.execute("select * from doctor_details where Doc_id=(%s)",(Doc_id,)) 
        z=y.fetchall()
        if z==[]:
            print('please enter correct id')
            continue
        else:
            Phno=input("Enter the correct phone no. : ")
            y.execute("update doctor_details set Phno =%s where Doc_id =%s",(Phno,Doc_id))
            print("----------------------Doctor's phone no. edited successfully----------------------")
            break
def editdoc():#funtion to edit doctor
    while True:
        print("-----------------------------------------")
        print("|To Edit doctor's department Enter 1    |")
        print("|To Edit doctor's name Enter 2          |")
        print("|To Edit doctor's address Enter 3       |")
        print("|To Edit doctor's phone number Enter 4  |")
        print("To go Back Enter B                      |")
        print("-----------------------------------------")
        Achoice=input("Enter your choice : ")
        Achoice=Achoice.upper()
        if Achoice == "1" :
            editdocdep()
            CONTINUE()
        elif Achoice == "2" :
           editdocname()
           CONTINUE()
        elif Achoice == "3" :
            editdocaddress()
            CONTINUE()
        elif Achoice == "4" :
            editdocphone()
            CONTINUE()
        elif Achoice == "B" :
            CONTINUE()
            break                 
        else :
            print("no record found ")

def viewfulldoctable():#function to view full doctor table
    y.execute('select * from Doctor_details')
    z=y.fetchall()
    for i in z:
        print('\n\n')
        l=len(i)
        for j in range(l):
            print(i[j],end='\t')

def dispdepuser():#function to display hospital depatments
    print("Hospital's departments :")
    y.execute("select distinct(Dept) from doctor_details")
    z=y.fetchall()
    for i in z:
        print('\n\n')
        l=len(i)
        for j in range(l):
            print(i[j],end='\t')

def dispdocuser():#funtion to display doctors
    print("Hospital's doctors :")
    y.execute("select Name from doctor_details")
    z=y.fetchall()
    for i in z:
        print('\n\n')
        l=len(i)
        for j in range(l):
            print(i[j],end='\t')

def docpatlst():#funtion to view list of patients treated by a particular doctor
    D_id= int(input("Enter doctor ID : "))
    y.execute("select Patient_Details.name from patient_details,doctor_details where patient_details.Doc_id=doctor_details.Doc_id and \
doctor_details.Doc_id=(%s)",(D_id,)) 
    z=y.fetchall()
    if z==[]:
        print('please enter correct id')
    else:
        print("list of patients being treated by doctor")
        for i in z:
            print('\n\n')
            l=len(i)
            for j in range(l):
                print(i[j],end='\t')
            

def deptpatlst():#function to view list of patients in a particular department
    Dept=input('enter dept')
    y.execute("select name from patient_details where Dept=(%s)",(Dept,)) 
    z=y.fetchall()
    if z==[]:
        print('please enter correct dept')
    else:
        print("list of patients in",Dept,"department")
        for i in z:
            print('\n\n')
            l=len(i)
            for j in range(l):
                print(i[j],end='\t')

def deptdoclst():#function to view list of doctors in a particular department
    Dept=input('enter dept')
    y.execute("select name from doctor_details where Dept=(%s)",(Dept,)) 
    z=y.fetchall()
    if z==[]:
        print('please enter correct dept')
    else:
        print("list of doctors in",Dept,"department")
        for i in z:
            print('\n\n')
            l=len(i)
            for j in range(l):
                print(i[j],end='\t')

def MYSql():#MYSql direct option to run customised commands
    while True:
        print('+-----------------------------------+')
        print('|  WELCOME TO MYSQL DIRECT          |')
        print('+-----------------------------------+')
        print('|To enter customised command Enter 1|')
        print('|To go back                  Enter 2|')
        print('+-----------------------------------+')
        MYSql_Direct=int(input('enter choice'))
        os.system('cls')
        if MYSql_Direct==1:
            n=input('enter command')
            y.execute(str(n))
            n.lower()
            if 'select' in n:
                z=y.fetchall()
                for i in z:
                    print('\n\n')
                    l=len(i)
                    for j in range(l):
                        print(i[j],end='\t')
                    
            CONTINUE()
        elif MYSql_Direct==2:
            break
        else:
            print('please enter correct option')
def CONTINUE():#function to check if the user would like to continue with program or to exit
    while True:
        c=input('\n\n\n would u like to continue y/n')
        c.lower()
        if c=='y':
            os.system('cls')
            break
        elif c=='n':
            sys.exit()
        else:
            print('\n\n\n enter correct option')
       
    
main()
x.close()

    
    
