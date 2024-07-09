from random import randrange

def randomNum():
    x=randrange(10)
    print("The random number was "+str(x))
    return x

def userNum():
    print("Enter your guess number")
    x=input()
    print("Your guess was "+x)
    return int(x)

def evaluates(gen,user):
    if (gen>user):
        return "too low"
    elif(user>gen):
        return "too high"
    elif(user==gen):
        return "you win!!!!!"

x=userNum()
y=randomNum()
#print(f"random is {y}")
print(evaluates(y,x))