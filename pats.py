def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('You can tell me your name or whatever.')
    name = input()
    print('The name suits the face, ' + name + '.')


def guess_age():
    print("Now, I'm going to blow your socks off.")
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + ". Huh, you have an old face.")


def count():
    print("Now I'm going to do something you probably can't: I will count to any number you enter.")

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Time to test your pop-culture knowledge.")
    print("What is the meaning of life?")
    answers = ["Live, laugh, love", "42", "To pass butter", "I don't know :("]
    for i in range(0, len(answers)):
        print(i+1, ". ", answers[i])
    while True:
        if int(input()) == 2:
            return print("Wow, look at you. You did it.")
        else:
            print("Wrong.")


def end():
    print("Thank god, it's over.")


greet('Passive-aggressive truth spewer, or PATS', '2020')
remind_name()
guess_age()
count()
test()
end()
