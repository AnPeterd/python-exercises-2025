def insertion_sort(numbers: list):
    for i in range (len(numbers)):
        for j in range(i):
            if int(numbers[i])<int(numbers[j]):
                a=numbers[i]
                del numbers[i]
                numbers.insert(j, int(a))
    return(numbers)


    
if __name__ == "__main__":
    c=((input('Skriv in dina tal:'))).split()
    flag=0
    for i in range(len(c)):
        if c[i].isdigit()==0:
            print('Vänligen ange endast tal!')
            flag=1
        else:
            c[i]=int(c[i])
    if flag ==0:
        print('Sorterat:')
        print(insertion_sort(c))