x = input("Do you want to stop the execution of the program (Y/N):\n")

if x.upper() == "Y":
    print("Bye!")

elif x.upper() == "N":
    name = input("Enter username:\n")
    passw = input("Enter password:\n")
    
    if name == "Pekka" and passw == "somerandomthing" :
        print("User recognized!")
        
    else:
        print(f"You entered an invalid login name and password.")
        
else:
    print("Invalid input! Please try again.")