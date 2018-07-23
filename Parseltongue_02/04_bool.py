a = ["false",True,True,None,True,None,None,False,False,None,True,False] 
b = ["or","or","or","==","!=","==","and","==","!=","and","!=","and"] 
c = [False,False,None,None,True,True,False,True,None,False,True,None]

def operand(x):
    if (b[x] == "or"):
        return a[i] or c[i]
    elif b[x] == "==":
        return a[i] == c[i]
    elif b[x] == "!=":
        return a[i] != c[i]
    elif b[x] == "and":
        return a[i] and c[i]

for i in range(len(a)):
    print(a[i],b[i],c[i], "=>", operand(i))
