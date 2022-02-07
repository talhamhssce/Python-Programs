#functions - is a combination of statement and block of code.
#name return parameter body
# declare
# define
# call

#type 1 - no parameters, no return
def add():
    print('Enter two numbers:')
    x = int(input())
    y = int(input())
    print('addition of two numbers is:', x+y)
add()

#type 2 - no parameters, with return value
def sub():
    print('Enter two numbers: ')
    x = int(input())
    y = int(input())

    return x-y

sub()
print('substraction of two numbers is:', sub())
