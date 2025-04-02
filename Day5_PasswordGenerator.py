#password Generator
import random
print("welcome to password generator")
n_letters= int(input("how many letters do you want in your password?"))
n_symbols = int(input("how many symbols do you want in your password?"))
n_numbers = int(input("how many numbers do you want in your password?"))
letters = ['A','b','C','d','e','f','g','H','I','j','k','L','M','n','o','p','Q','r','S','T','u','v','w','X','Y','Z']
symbols= ['!',"@","#",'&','$']
numbers = ['1','2','3','4','5','6','7','8','9','0']
list_password = []
for i in range(0,n_letters):
    list_password.append(random.choice(letters))
for i in range(0,n_symbols):
    list_password.append(random.choice(symbols))
for i in range(0,n_numbers):
    list_password.append(random.choice(numbers))
random.shuffle(list_password)
password = ''
for i in list_password:
    password += i
print(f'Your password is : {password}')
