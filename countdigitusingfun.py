def count_digit(n):
    print(n)
    while n>0:
        r=n%10
        n=n/10
    print(r)
n=int(input("enter numbers"))
count_digit(n)
