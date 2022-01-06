from cryptography.fernet import Fernet 
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key



key = load_key()
fer = Fernet(key)

# main_pass=input("Enter your main password : ")



def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip();
            user, passw =data.split("|")
            print("User: " , user ,"| Password: ", fer.decrypt(passw.encode()).decode())

def add():
    Name=input("Enter the Account Name\n")
    pwd=input("Enter the Password")

    with open('password.txt', 'a') as f:
        f.write(Name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        

while True:
    mode=input("what would you like to do \n1.View\n2.Add\n3.Quit\n" )
    if mode.lower() == "quit":
        quit()
    if mode.lower() =="view":
        view()
    if mode.lower() =="add" :
        add()

