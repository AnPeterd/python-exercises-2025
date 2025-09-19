tal=float(input())
summ=0 
counter=0
maxi=float('-inf')
mini=float('+inf')
while tal!=0:
    if tal<mini:
        mini=tal
    if tal>maxi:
        maxi=tal
    summ+=tal
    counter+=1
    tal=float(input())
summ-=mini
summ-=maxi
counter-=2
medelvardet=summ/counter
print(medelvardet)
