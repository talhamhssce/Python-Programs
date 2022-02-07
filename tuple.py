#Tuple is immutable
#here () bracket is used which is known as paranthesis

t = (1, 2, 3, 4, 5)
print(t)

print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[2:])

u = (100,200) + t[2:]
print(u)

v = (t,u)
print(v)

names = ['john','paul', 'george', 'ringo']
z = (t,names)
print(z)

z[1][1] = 'Talha'
print(z)