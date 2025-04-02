import art

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2


def multiply(n1,n2):
    return n1*n2


def divide(n1,n2):
    return n1/n2

operations_dictionary= {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    }


def calculator():
    print(art.logo)
    n1 = float(input('Enter first number: '))
    should_continue = True
    while should_continue:
        for key in operations_dictionary:
            print(key)
        operation = input("please select operation to be performed: ")
        n2 = float(input('Enter second number: '))
        result = operations_dictionary[operation](n1,n2)
        print(f'{n1} {operation} {n2}= {result}')
        user_choice = input(f'Type "yes" do you want to continue to do calculation with the previous result {result}, type "no" if you want to start new calculation, type "exit" if you want to exit from the calculator: ').lower()
        if user_choice == 'no':
            should_continue = False
            print("\n"*20)
            calculator()
        elif user_choice == 'yes':
            n1 = result
        else:
            print("Thanks")
            should_continue = False
            

calculator()