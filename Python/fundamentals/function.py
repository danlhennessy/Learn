def saysomething():
    print("something")
    
saysomething()

#Require 'name' as a parameter when calling function 'say_hi'
def say_hi(name):
    print(f"Hello {name}")

#'dan' is the argument passed into the function    
say_hi("dan")

#Variable number of arguments (*args and **kwargs) https://www.geeksforgeeks.org/args-kwargs-python/

def myFun(*argv): 
    for arg in argv: 
        print (arg)
    
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 


def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
      
# Now we can use *args or **kwargs to
# pass arguments to this function : 
args = ("Geeks", "for", "Geeks")
myFun(*args)
  
kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"}
myFun(**kwargs)