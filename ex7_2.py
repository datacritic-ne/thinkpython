import math

def eval_loop():
    
    #string = str(input("Give me some input: "))

    while True:
    
        string = input("> ")
        
        if string == 'done':
            break
        else:
            y = eval(string)
            print(y)

    print(y)
        #string != 'done':
        #print(eval(string))
        #eval_loop()

eval_loop()