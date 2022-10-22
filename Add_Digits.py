n=int(input())
s=n
while True: 
    n=s
    s=0
    while n:
        r=n%10
        n=n//10
        s=s+r
    if s<=9:
        break
print(s)