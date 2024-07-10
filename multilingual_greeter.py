#Exercise2
def language_input() -> int:
    print("Please choose a language: ")
    print("1 - English")
    print("2 - Spanish")
    print("3 - Portuguese")
    return int(input())


def name_input(lang_choice: int) -> str:

    prompt = None

    if lang_choice == 2:
        prompt = "¿Cómo te llamas?\n"
    elif lang_choice == 3:
        prompt = "Qual é o seu nome?\n"
    else:
        prompt = "What is your name?\n"

    return input(prompt)


def greet(name: str, lang_choice: int) -> None:

    greeting = None

    if lang_choice == 2:
        greeting = "Hola " + name
    elif lang_choice == 3:
        greeting = "Olá " + name
    else:
        greeting = "Hello " + name
    
    print(greeting)


lang_choice = language_input()
name = name_input(lang_choice)
greet(name, lang_choice)

"""
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
"""