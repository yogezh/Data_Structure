print('''
********************************************************************************
****  DATA STRUCTURE TO ADD AND DELETE AN ELEMENT IN A LIST UNTIL USER QUIT ****
********************************************************************************
''')
stack = []
def push ():
    element = int(input("Enter your Element : "))
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("Stack is Empty! Please Add some Elements by pressing 1 ")
    else:
        delete = stack.pop()
        print("Deleted Successfully : ",delete)
        print(stack)
def display():
    if not stack:
        print("Nothing to Display so please Add Elements by pressing 1 ")
    else:
        print("Your Elements are : ")
        for i in stack:
            print(i)

while True:
    print(''' 
    (1) Press 1 to Add an Element
    (2) Press 2 to Delete an Element
    (3) Press 3 to Display all the Elements
    (4) Press 4 to Quit 
    ''')
    choice = int(input("Choose the Operation you want to perform : "))
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()
    elif choice==4:
        print(stack)
        break
    else:
        print("Please enter the Correct Option")