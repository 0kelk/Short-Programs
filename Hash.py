import time
password = hash("password") #Inital password is "password"
access = False
finish = False
while finish == False:
    while access == False:
        attempt = input("Please input your password:\n") #Asks for password
        if hash(attempt) == password: #Grants access if hashed attempt matches the stored hash
            print("Access Granted")
            access = True
            finish = True
        else:
            print("Access Denied, please try again.") #Denies access if hashed attempt does not match the stored hash
    changepass = input("Would you like to change your password? y/n\n") #Everything from this point is shown when access is granted #Asks if user would like to change password
    if changepass == "y": #If the answer is yes
        newpass = input("What would you like to change it to?\n") #Asks what to change it to
        password = hash(newpass) #Replaces the old hash with the new one
        print("Logging out...") #Logs out
        time.sleep(2)
        access = False #Redirects user back to 'Please input your password'
        finish = False
    if changepass == "n": #If the answer is no, finishes program
        print("Closing program...")
