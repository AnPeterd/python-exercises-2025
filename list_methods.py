capitals = ["Amsterdam", "Tokyo", "London", "Stockholm"]
print(capitals)
print(capitals[0])
capitals.append("Paris")
print(capitals)
print(capitals[1:3])
#for i in range(len(capitals)//2):
#    capitals[i], capitals[-i-1] = capitals[-i-1], capitals[i]
capitals.reverse()
print(capitals)
capitals.append("Stockholm")
print(capitals)
print(capitals.count("Stockholm"))
capitals.remove("Stockholm")
print(capitals)
print(len(capitals))
capitals.insert(0,100)
print(capitals)
capitals[0]="Washington"
print(capitals)
