# Q.19 How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.
  
#   specify the code that is executed when control leaves the try block,

def divide(x, y): 
    try: 
        result = x // y 
        print("Yeah ! Your answer is :", result) 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ") 
divide(3, 2) 
divide(3, 0)
