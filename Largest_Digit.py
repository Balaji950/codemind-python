n=int(input())
mx=0
while n>0:
    r=n%10
    n=n//10
    mx=max(mx,r)
print(mx)
    