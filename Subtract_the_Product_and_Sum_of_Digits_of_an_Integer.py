n=int(input())
s=1
t=0
while n>0:
    r=n%10
    s=s*r
    t=t+r
    e=s-t
    n=n//10
print(e)
    