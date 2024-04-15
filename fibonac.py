def fibonacia(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacia(n-1)+fibonacia(n-2)
a=fibonacia(20)
print(a)