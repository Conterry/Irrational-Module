error = 0

def crear_error():
    error = 0
    return

def add(a, b):
    try:
        if(a[1]==b[1]):
            x = a[0]+b[0]
            y = a[1]
        else:
            x = a[0]*b[1]+a[1]*b[0]
            y = a[1]*b[1]
        return (x,y)
    except:
        error+=1
        return(None, None)

def mul(a, b):
    try:
        x = a[0]*b[0]
        y = a[1]*b[1]
        return (x,y)
    except:
        error+=1
        return(None, None)

def sub(a, b):
    try:
        x = a[0]*b[1]-a[1]*b[0]
        y = a[1]*b[1]
        return (x,y)
    except:
        error+=1
        return(None, None)
    
def div(a, b):
    try:
        if(type(a)==int): a=(a,a)
        if(type(b)==int): a=(b,b)
        x = a[0]*b[1]
        y = a[1]*b[0]
        return (x,y)
    except:
        error+=1
        return(None, None)
    
def create(m, n):
    if(n == "" or n == 0):
        return(None, None)
    return (m, n)

def inp():
    try:
        return create(float(input()), float(input()))
    except:
        error+=1
        return(None, None)
    
def prt(a):
    print ("=====================")
    print (int(a[0]))
    print ('--')
    print (int(a[1]))
    return

def _reduce(a):
    try:
        gcf = 1
        for i in range(int(max(a[0], a[1])), 0, -1):
            if(a[0]%i==0 and a[1]%i==0):
                gcf = i
                break
        return(a[0]/gcf, a[1]/gcf)
    except:
        error+=1
        return(None, None)

def eq(a, b):
    return True if _reduce(a) == _reduce(b) else False

def it(a, b):
    return True if _reduce(a) < _reduce(b) else False
