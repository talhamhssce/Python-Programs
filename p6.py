print('enter the marks of p,c,m')

p = int(input('enter the marks of p:'))
c = int(input('enter the marks of c:'))
m = int(input('enter the marks of m:'))

avg = (p+c+m)/3
print('the average is:', avg)

if avg >= 75:
    print('A garde')
elif avg >= 65:
    print('B grade')
elif avg >= 55:
    print('C grade')
elif avg >= 45:
    print('D grade') 
else:
    print('fail')           
