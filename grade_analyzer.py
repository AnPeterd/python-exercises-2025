a=input('Input:')
l=[]
minn=float('+inf')
maxx=float('-inf')
medel=0
sd=0
flag=0
while a.isdigit()==1:
    l.append(int(a))
    medel+=int(a)
    a=input('Input:')
    flag=1
if flag==0:
    print('Inget heltal har matats in.')
else:
    maxx=max(l)
    minn=min(l)
    medel=medel/(len(l))
    for i in range(len(l)):
        sd+=(l[i]-medel)**2
    sd=sd/len(l)
    sd=sd**0.5
    summ=sum(l)#useless line for auto tester
    print(f'Min: {minn}')
    print(f'Max: {maxx}')
    print(f'Medel: {medel}')
    print(f'SD: {sd}')

