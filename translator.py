




english_to_german = {
		"good day": "Guten Tag!",
		"good morning": "Guten Morgen!",
		"goodbye": "Auf Wiedersehen!",
		"how are you": "Wie geht's?",
		"my name is python": "Mein Name ist Python!",
		"do you speak english": "Sprechen sie Englisch?",
		"where is the bathroom": "Wo ist die Toilette?",
		"thank you": "Danke!",
		"i am sorry": "Es tut mir leid!",
		"a large beer please": "Ein grosses Bier, bitte!"
}
word=input('Skriv en engelsk mening att översätta:')
word=word.lower()
symbols="!#$%&()*+,-./:;<=>?@[\]^_`{|}~"
word=list(word)
word1=[]
for i in range(len(word)):
    if word[i] not in symbols:
        word1.append(word[i])
word=''
for i in word1:
    word+=i
if word not in english_to_german:
    print('Ingen översättning hittades!')
else:
    print(english_to_german[word])
    
