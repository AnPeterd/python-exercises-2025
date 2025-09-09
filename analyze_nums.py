with open('numbers.txt', 'r', encoding='utf-8') as f:
    a=f.readlines()
    b={}
    for i in range(len(a)):
        a[i]=a[i].strip()
        if a[i] in b:
            b[a[i]]+=1
        else:
            b[a[i]]=1
print("---------------")
print("- NUMANALYZER -")
print("---------------")
for i, j  in b.items():
    print(f"{i:>2} | {j:>6}")
print("---------------")
with open('number_report.txt','w', encoding='utf-8') as w:
    w.write("---------------\n")
    w.write("- NUMANALYZER -\n")
    w.write("---------------\n")
    for i, j  in b.items():
        w.write(f"{i:>2} | {j:>6}\n")
    w.write("---------------\n")

