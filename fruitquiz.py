
import random


class FruitQuiz:
    
    
    def __init__(self):
        self.fruits = {
            "apple": "red",
            "banana": "yellow",
             "orange": "orange",
             "watermelon": "green",
        }

    
    def quiz(self):
        
        
        while True:
            
            
            fruit, color = random.choice(list(self.fruits.items()))
            
            
            print("\nWhat is the color of", fruit, "?")
            
           
            user_answer=input()

            if user_answer.lower() == color:
                print("Correct!")
            else:
                print("Wrong! The correct answer is", color)
            options=int(input("Do you want to continue? (1 for yes, 0 for no):"))
            if options==0:
                print("Thank you for playing!")
                break


            
        
          


print("Welcome to Fruit Quiz")


fq = FruitQuiz()

fq.quiz()