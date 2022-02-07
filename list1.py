fruits = ['mango', 'apple', 'banana', 'orange', 'strawberry']
print(fruits)
print(fruits[0])
print(fruits[1])

fruits.sort() #it is used to sort the list in alphabatical order

# here we iterate using for loop
for f in fruits:
    print(f)
    if 'banana' in f:
        print('i like banana')
