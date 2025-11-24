import random

letters = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z"]
number = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*","(",")","-"]

passwords_db = {}

def generate_password(n1, n2, n3):
    stuff = []
    for _ in range(n1):
        stuff.append(random.choice(letters))
    for _ in range(n2):
        stuff.append(random.choice(symbols))
    for _ in range(n3):
        stuff.append(random.choice(number))
    random.shuffle(stuff)
    return "".join(stuff)

def add_password(app, pwd):
    passwords_db[app] = pwd
    print("Password for '" + app + "' added.")

