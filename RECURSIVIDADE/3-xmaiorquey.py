x = 1
y = 8

def f(x,y):
    if (x>=y):
        return (x+y)/2
    else:
        return f( f((x+2),(y-1)),f((x+1),(y-2)) )
print(f(1,8))