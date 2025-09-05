def unique_items(lst):
    unique=[]
    for i in range(len(lst)):
        if unique.count(lst[i])==0:
            unique.append(lst[i])
    return unique
if __name__ == "__main__":
    def main():
        nationalities = [
		    "USA",
		    "Brasilien",
		    "Tyskland",
		    "Spanien",
		    "Nederländerna",
		    "USA",
		    "USA",
		    "Australien",
		    "Japan",
		    "Egypten",
		    "Sverige",
		    "Sydkorea",
		    "Kina",
		    "Japan",
		    "Mexico",
		    "Tyskland",
		    "Sverige",
		    "Nederländerna",
		    "Kanada"
        ]
        print(unique_items(nationalities))
    main()