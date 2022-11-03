n=int(input())
t=n
k=t*t
s=0
while k:
    r=k%10
    s+=r
    k=k//10
if n==s:
    print('Neon Number')
else:
    print('Not Neon Number')