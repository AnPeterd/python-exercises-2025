def validate_pwd(string):  #The worst code of my life, I wiil rewrite it
    string=str(string)
    if len(string)<6 or len(string)>16 or (string.find('$')==-1 and string.find('!')==-1 and string.find('@')== -1 and string.find('*')==-1):
        print ('Lösenordet duger inte, vänligen försök igen!')
        return(False)
    if string.upper() == string or string.lower()== string:
        print ('Lösenordet duger inte, vänligen försök igen!')
        return(False)
    numberflag=0
    for i in range(len(string)):
        if not (65<=ord(string[i])<=90 or 97<=ord(string[i])<=122 or 48<=ord(string[i])<=57 or string[i]=='@' or string[i]=='*' or string[i]=='!' or string[i]=='$'):
            print ('Lösenordet duger inte, vänligen försök igen!')
            return(False)
        if 48<=ord(string[i])<=57:
             numberflag=1
    if numberflag==0:
            print ('Lösenordet duger inte, vänligen försök igen!')
            return(False)
    print('Bra val!')
    return(True)

if __name__ == "__main__":
          
          print ('Välkommen till DV1574WebApps lösenordsvalidering')
          print ('------------------------------------------------')
          a=input('Välj ett lösenord:')
          b=False
          while b==False:
               b=validate_pwd(a)
               if b==False:
                   a=input('Välj ett lösenord:')
print('Programmet avslutas ... ')
