def doSomesthing(*args, **keywords):
    for i in args:
        print(i)
    for k,v in keywords.items():
        print(k,v) 

doSomesthing(1,2,3,4,5, {1: 'a', 2: 'b', 3: 'c'})