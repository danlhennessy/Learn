class Chef:
    def make_chicken(self):
        print("Chef makes a chicken")
        
    def make_salad(self):
        print("Chef makes a salad")
        
    def make_special(self):
        print("Chef makes the special")

#ChineseChef class imports all functions from inside Chef class        
class ChineseChef(Chef):
    #If you define a new function that exists in inherited class, the new function overrites the original
    def make_special(self):
        print("Chef makes noodles")
    def make_fried_rice(self):
        print("Chef makes fried rice")
    
mychef = Chef()
mychef.make_chicken()

mychinesechef = ChineseChef()
mychinesechef.make_special()