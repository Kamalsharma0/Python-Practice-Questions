#impliment break, continue and pass

correct_password = "Kamal@123"

while True:
    user_password = input("Enter Password: ")

    if user_password == "":
        pass
        print("You did not enter anything, please try again!")
        continue

    if user_password == correct_password:
        print("Password is Correct")
        break
    else:
        print("Password is incorrect, Try")



