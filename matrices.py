def read_matrix():
    b=[]
    print('Ange din matris:')
    while (a:=input('')):
        b.append(a)
    for i in range(len(b)):
        b[i]=str(b[i]).split()
    for i in range(len(b)):
        for j in range(len(b[i])):
            b[i][j]=int(b[i][j])
    return(b)


def scalar_multiplication(matrix, scalar):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j]=int(matrix[i][j])*scalar
    return(matrix)

def transpose (matrix):
    b=[]
    for i in range(len(matrix[0])):
        b.append([])
    for i in range(len(matrix)):#2
        for j in range(len(matrix[i])):#3
            b[j].append(matrix[i][j])
    return(b)
            



if __name__ == "__main__":
    a=read_matrix()
    print(f'Din matris:\n{a}')
    print(f'Skalär multiplikation med 8 blir:\n{scalar_multiplication(a,8)}')
    for i in range(len(a)):# This is here because other functions change a
        for j in range(len(a[i])):
            a[i][j]=int(a[i][j])//8
    print(f'Transponering blir:\n{transpose(a)}')


