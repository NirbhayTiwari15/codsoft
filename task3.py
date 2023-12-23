import random,string
print("Welcome to Password Generater")
n=int(input("Enter the length of password you want to generate:"))
password=""
for i in range(n):
    p=random.choice(string.ascii_letters+string.digits)
    password+=p
print(password)