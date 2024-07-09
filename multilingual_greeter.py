#Exercise2
def greet(name):
    print("Hi "+name)

def name_input():
    return input("Hi, what's your name?")

def language_input(name):
    print("choose the reply in the following language: \n1. Japanese\n2. Chinese\n3. France")
    choice = input()
    if(choice=='1'):
        print("こんにちは, "+name)
    elif(choice=='2'):
        print("哈喽, "+name)
    elif(choice=='3'):
        print("Salut, "+name)
    else:
        print("invalid input")

language_input(name_input())