try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Exception caught")
else:
    print("Everything went wrong")
finally:
    print("'finally' block is always executed")
    

x = -1
if x < 0:
    raise Exception("Number is below zero")