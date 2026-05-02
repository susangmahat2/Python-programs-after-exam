class flashcard:
    def __init__(self, word, meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word +"("+self.meaning +")"
flash=[]
print("welcome to flashcard application")    
while True:
    word=input("enter the word:")
    meaning=input("enter the meaning:")
    flash.append(flashcard(word,meaning))
    options=int(input("do you want to add more flashcards? (1 for yes, 0 for no):"))
    if(options==0):
        break
print("\nYour flashcards:")
for i in flash:
    print(">",i)    
