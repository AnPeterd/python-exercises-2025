def validate_pnr (nr_string):
    nr_string=str(nr_string)
    if len(nr_string)!=10 or nr_string.isnumeric()==0 :
        return(False)
    else:
        summ=0
        for i in range (len(nr_string)-1):
            if i%2==0:
                a=str(int(nr_string[i])*2)
                for j in range(len(a)):
                    summ+= int(a[j])
            else:
                a=str(int(nr_string[i]))
                for j in range(len(a)):
                    summ+= int(a[j])
        summ=str(summ)
        if (int(summ[0]))*10 - int(summ)== int(nr_string[-1]) or (int(summ[0]))*10+10 - int(summ)== int(nr_string[-1]):
            print('OK - Personnumret är giltigt')
            return(True)
        print('FEL - Personnumret är ogiltigt')
        return(False)
        

if __name__ == "__main__":
    print('Välkommen till ”Personnummer-kollen”')
    print('-------------------------------------')
    pnr=input('Ange ett personnummer med 10 siffror:')
    flag="J"
    while flag!="N":
        validate_pnr(pnr)
        flag=input('Vill du kontrollera fler personnummer (J/N)?')
        if flag=='J':
            pnr=input('Ange ett personnummer med 10 siffror:')
    print('Programmet avslutas ..')
        