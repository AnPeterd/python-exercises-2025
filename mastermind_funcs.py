import random
def generate_code():
    a=[]
    for i in range(4):
        a.append(random.randint(0,5))
    return(a)

def right_position(guess, code):
    counter=0
    for i in range(min(len(guess), len(code))):
        if guess[i]==code[i]:
            counter+=1
    return(counter)
        
    
def wrong_position(guess, code):
    counter = 0
    code_copy = code.copy()  
    
    for i in range(min(len(guess), len(code))):
        if guess[i] == code[i]:
            code_copy[i] = None
    
    for i in range(min(len(guess), len(code))):
        if guess[i] != code[i] and guess[i] in code_copy:
            counter += 1
            code_copy[code_copy.index(guess[i])] = None
    return counter
    

