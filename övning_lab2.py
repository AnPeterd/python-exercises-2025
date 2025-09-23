def fun(list1,list2,value):
    for i in range(len(list1)):
        if list2[i]==value:
            list1[i]=value
    print(list1)
    for i in range(len(list2)):
        print(list2[i])
    return 0

list1 = eval(input())
list2 = eval(input())
value = eval(input())
fun(list1,list2,value)