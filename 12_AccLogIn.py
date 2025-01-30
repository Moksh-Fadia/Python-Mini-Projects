import string
import os

def signIn():
    if not os.path.exists("saved.txt"):
        print("No accounts made yet.")
        return

    usr = input("Enter username: ")
    pwd = input("Enter password: ")

    with open("saved.txt", "r") as f:
        accounts = f.readlines()        #This reads all accounts and stores them in a list (one line per account).
    
    for account in accounts:
        saved_usr, saved_pwd = account.strip().split(",")       

        if saved_usr == usr and saved_pwd == pwd:
            print("------Signed in successfully------")
            print(f"Welcome, {usr}!")
            break

    print("Incorrect username or password.")        
            


def register():
    usr = input("Create username: ")

    with open("saved.txt", "r") as f:
        accounts = f.readlines()

    for account in accounts:
        saved_usr, saved_pwd = account.strip().split(",")        
        if saved_usr == usr:
            print("Username already exists! Try another username.")
            return    

    while True:
        pwd = input("Create password: ")

        if not (8 <= len(pwd) <= 12):
            print("Password should be between 8-12 characters!") 
            continue

        if not any(char in string.punctuation for char in pwd):
            print("Password should contain atleast 1 special character")    
            continue

        while True:    
            confirm_pwd = input("Confirm password: ")

            if pwd == confirm_pwd:
                break
            else:
                print("Passwords do not match! Try again.")
        break    

    with open("saved.txt", "a") as f:
        f.write(f"{usr},{pwd}\n")

    print(f"Hello, {usr}! You've successfuly made an account.")        


def delete():
    if not os.path.exists("saved.txt"):
        print("No accounts made yet.")
        return

    usr = input("Enter account to delete: ")
    pwd = input("Enter password: ")

    with open("saved.txt", "r") as f:
        accounts = f.readlines()

    updated_accs = []       # Store accounts that we want to keep
    acc_deleted = False

    for account in accounts:
        saved_usr, saved_pwd = account.strip().split(",")        

        if saved_usr == usr and saved_pwd == pwd:
            acc_deleted = True          # Account found, mark for deletion
        else:
            updated_accs.append(account)    # Append/Keep other accounts 

    if acc_deleted:
        with open("saved.txt", "w") as f:
            f.writelines(updated_accs)
        print(f"Account {usr} successfully deleted")         # Overwrite file with remaining accounts
    else:
        print("Account not found or incorrect password.")    



def main():
    while True:
        ask = input("Sign In / Register / Delete / Exit : ").lower().replace("  ", " ")

        if ask == 'register':
            register()
        elif ask == 'signin':
            signIn()
        elif ask == 'delete':
            delete()
        elif ask == 'exit':
            break
        else:
            print("Invalid option. Try again.")   

main()