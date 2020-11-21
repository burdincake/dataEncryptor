import base64
import json
def setPassword():
    file = open("credentials.txt","r")
    a = file.read()

    if a=="":
        print('insert new Password: ', end='')
        password = input()
        password = password.encode("UTF-8")
        x = 1
        while x <= 5:
            password = base64.b64encode(password)
            x = x + 1
        password = password.decode("UTF-8")
        passfile = open("credentials.txt", "w")
        passfile.write(password)
        passfile.close()
        print("your base64 encoded password = ", password)
    else:
        print("You have exsisting password. To change password, enter current password: ",end="")
        inputer = input()
        for x in range(5):
            inputer = base64.urlsafe_b64encode(bytes(inputer, 'UTF-8')).decode("UTF-8")

        if a == inputer:
            print('insert new Password: ', end='')
            password = input()
            password = password.encode("UTF-8")
            x = 1
            while x <= 5:
                password = base64.b64encode(password)
                x = x + 1
            password = password.decode("UTF-8")
            passfile = open("credentials.txt", "w")
            passfile.write(password)
            passfile.close()
            print("your base64 encoded password = ", password)
        else:
            print("SYSTEM: password not matching!")
    login()
    file.close()
def menu():
    print("Enter among (View / Append / Reset): ",end="")
    enter = input()

    if enter == "view" or enter == "View":
        hash = open("hash.txt")
        print("**************************************")
        for line in hash:
            a = base64.urlsafe_b64decode(bytes(line, 'UTF-8')).decode("UTF-8")
            print(a)
        a = hash.read()
        print("**************************************")
        print("\n")
        hash.close()
        menu()
    elif enter == "append" or enter == "Append":
        print("enter the link you want to save (ex: \"name: www.example.com\"): ",end="")
        save = input()
        encryptionSave = base64.urlsafe_b64encode(bytes(save, 'UTF-8')).decode("UTF-8")
        print(encryptionSave)
        filemake = open("hash.txt","a")
        filemake.write("\n")
        filemake.write(encryptionSave)
        filemake.close()
        print("encrypted append Success :)")
        menu()
    elif enter == "reset" or enter == "Reset":
        print("Do you want to reset your hash script? (Yes / No): ")
        answer = input()
        if answer == "yes" or answer =="Yes":
            hashfile = open("hash.txt","w")
            hashfile.write("")
            hashfile.close()
            print("SYSTEM: reset have been successfully finished! :)")
        else:
            print("SYSTEM: Reset has been cancled! :)")
    elif enter == "exit" or "logout":
        exit()
    else:
        menu()




def login():
    print("Enter ID: ",end="")
    id = input()
    print("Enter Password: ",end = "")
    e = input()
    enteredPwd = e.encode("UTF-8")
    x=1
    while x<=5:
        enteredPwd = base64.b64encode(enteredPwd)
        x=x+1
    enteredPwd = enteredPwd.decode("UTF-8")
    passfile = open("credentials.txt","r")
    realPwd = passfile.read()
    if realPwd == enteredPwd:
        print("Welcome hidden user :)")


        

        menu()
    else:
        print("Bye")



# setPassword()
#login()

a = """
█▀▄▀█ ██      ▄▄▄▄▄    ▄▄▄▄▄          ▄▄▄▄▄   ▄███▄   ▄█▄      ▄   █▄▄▄▄ ▄███▄          ▄▄▄▄▄      ▄▄▄▄▀ ████▄ █▄▄▄▄ ██     ▄▀  ▄███▄   
█ █ █ █ █    █     ▀▄ █     ▀▄       █     ▀▄ █▀   ▀  █▀ ▀▄     █  █  ▄▀ █▀   ▀        █     ▀▄ ▀▀▀ █    █   █ █  ▄▀ █ █  ▄▀    █▀   ▀  
█ ▄ █ █▄▄█ ▄  ▀▀▀▀▄ ▄  ▀▀▀▀▄       ▄  ▀▀▀▀▄   ██▄▄    █   ▀  █   █ █▀▀▌  ██▄▄        ▄  ▀▀▀▀▄       █    █   █ █▀▀▌  █▄▄█ █ ▀▄  ██▄▄    
█   █ █  █  ▀▄▄▄▄▀   ▀▄▄▄▄▀         ▀▄▄▄▄▀    █▄   ▄▀ █▄  ▄▀ █   █ █  █  █▄   ▄▀      ▀▄▄▄▄▀       █     ▀████ █  █  █  █ █   █ █▄   ▄▀ 
   █     █                                    ▀███▀   ▀███▀  █▄ ▄█   █   ▀███▀                    ▀              █      █  ███  ▀███▀   
  ▀     █                                                     ▀▀▀   ▀                                           ▀      █                
       ▀                                                                                                              ▀                 
"""
print(a)
print("Hello! Welcome to data secure storage :)")
print("you can store your data which is absolutly inapproachable without your password!!")

login()