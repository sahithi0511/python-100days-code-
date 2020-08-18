def count_digit(n):
    c=0
    while (n):
        r=n%10
        c=c+1
        n=n//10
    print(c)
n=int(input("enter numbers"))
count_digit(n)
