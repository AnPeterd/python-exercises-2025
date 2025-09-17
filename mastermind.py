import mastermind_funcs
print('Welcom to the game Master Mind')
code=mastermind_funcs.generate_code()
a=(input('I have generated a code, lets begin guessing. Your first gues:')).split()
for i in range(len(a)):
    a[i]=int(a[i])
counter =1
while a!=code:
    counter+=1
    print('Right position', mastermind_funcs.right_position(a, code))
    print('Wrong position', mastermind_funcs.wrong_position(a, code))
    a=input(f'Your attmpt number {counter} :').split()
    for i in range(len(a)):
        a[i]=int(a[i])
print('Solved!')