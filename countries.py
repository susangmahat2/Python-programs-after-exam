class India:
    def capital(self):
        print("The capital: New Delhi")
    def language(self):
        print("The Language: Hindi")    
    def type(self):
        print("the type:develping country")
class USA:
    def capital(self):
        print("The capital: Washington, D.C.")
    def language(self):
        print("The language: English")
    def type(self):
        print("The type: Developed country")

obj_ind=India()
obj_usa=USA()

for country in(obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()
