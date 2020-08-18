def asc_dsc(n):
    asc=0
    dsc=0
    r=n%10
    r1=r
    while n:
        r=n%10
        if(r1>r):
            asc=asc+1
            r1=r
        elif(r1<r):
            dsc=dsc+1
            r1=r
        n=n//10
    if(asc!=0 and dsc==0):
        print("Ascending number")
    elif(asc==0 and dsc!=0):
        print("Descending number")
    elif(asc!=0 and dsc!=0):
        print("mixed number")
n=int(input("Enter number"))
asc_dsc(n)
