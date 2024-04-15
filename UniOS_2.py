# import genpas
import time
import os
print("Hello!")
information = "" # информация в серверах
name1 = "" 
tim = 7
teas = []
teasx = ""
teasx2 = ""
teasx3 = ""
q1 = ""
password1 = ""
passw = []
info = []
name = input("Login: ")
password = int(input("Password: "))
os.system("cls")
nam = []
# print(genpas.generate_password())
ths = ""         
print("""
          #########   #########
          1/console   4/strings
          #########   #########
          
          #########   #########
          2/servers   5/files12
          #########   #########
          
          #########   #########
          3/purpose   6/close12
          #########   #########
          
          
                                                               """)
def look():
     look1 = input(" ")
     print(look1)
def string():
     global teas, teasx, teasx2, teasx3, q1
     teasx = input("")
     teas.append(teasx)
     teasx2 = input("Новая строчка? ")
     if teasx2 == "Да":
             teasx3 = input("")
             teas.append(teasx3)
     print(teas)
     q1 = input("Сохранено! ")
def collect():
          input(" ")
def wbx():
     global look3
     look3 = input(" ")
def nbx():
          look4 = int(input( ))
def lookf():
          look5 = input( )
def deletef():
          print("Error")
def createf():
          look6 = input( )
          look7 = input(" ")
          print(look6, look7)
def look111():
          print("Error") 

def num1():
     qwert = input("Command: ")
     print("""Commands: 
               look
               collect
               wbx
               nbx
               look /f
               delete /f
               create /f
               note### /f
               look###
                              """)
def num2():
     print("""Actions: 
                    Search
                    Create
                    Join
                                                  """)
def search():
          print(nam)
def create():  
     global name1, password1, nam, passw, information
     
     # nam = input("Name of server: ")
     name1 = input("Введите имя сервера: ")
     nam.append(name1)
     password1 = int(input("Введите числовой пароль: "))
     passw.append(password1)    
     information = input("Информация/данные для сервера: ")
     info.append(information)

# def join():
#      global do1, do2, t, do3, password1, name1, nam, information
#      print(nam)
#      do1 = input("Ваши действия: ")
#      if do1 == "Join":
#           do2 = input("Name: ")
#           if do2 == name1:
#                print("Подключение...")
#                t = 10
                    
#                while t >= 0:
#                     time.sleep(1)
#                     t -= 1                                                
#                do3 = int(input("Введите пароль: "))
#                if do3 == password1:
#                     print(information)
#                else:
#                     print("Error")
def join():
    global do1, do2, t, do3, password1, nam, information
    print(nam)
    do1 = input("Ваши действия: ")
    if do1 == "Join":
        do2 = input("Name: ")
        if do2 in nam:
            print("Подключение...")
            t = 10
            while t >= 0:
                time.sleep(1)
                t -= 1
            index = nam.index(do2)
            do3 = int(input("Введите пароль: "))
            if do3 == passw[index]:
                print(info[index])
            else:
                print("Error")
        else:
            print("Server not found")

def files():
      print(ths,teas,teasx,teasx2,teasx3,q1)


def purpous():
          global thx
          thx = input(" ")
def exit():
     quit()
          
def proverka():         
     qwerty = int(input("Подтвердите пароль: "))
     if qwerty == password:
          print("Вы подтвердили пароль!!! ")
     else:
          quit()
while True:
     proverka()         
     rew = int(input("Numder: "))
     if rew == 1:
          num1()
          rew2 = int(input("Number: "))
          if rew2 == 1:
               look()
          elif rew2 == 2:
               collect()
          elif rew2 == 3:
               wbx()
          elif rew2 == 4:
               nbx()
          elif rew2 == 5:
               lookf()
          elif rew2 == 6:
               createf()
          elif rew2 == 7:
               look111()
          elif rew2 == 8:
               deletef()           
          else:
               print("Error")
     elif rew == 2:
          num2()
          rew3 = int(input(" "))
                    
          if rew3 == 1:
               search()
          elif rew3 == 2:
               create()
          elif rew3 == 3:
               join()
     elif rew == 6:
          print("Завершение работы...")
          while tim >= 0:
               time.sleep(1)
               tim -= 1
               quit()
               
     elif rew == 3:
          purpous()
     elif rew == 4:
          string()
     elif rew == 5:
          files()


     