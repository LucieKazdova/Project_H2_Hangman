# HANGMAN GAME - final version

import random

print("H A N G M A N")

# 1.porovnání výběru vlastního slova s počítačem, když stejný - survive, jiný - lost

"""word = input("Guess the word: > ")

list = ["python", "java", "swift", "javascript"]

computer = random.choice(list)
if word == computer:
    print ("You survived!")
else:
    print("You lost!")"""

# 2. počítač vybere slovo a napoví jen ukázkou prvních 3 písmen, pokud uživatel správně dopíše - survive, jinak lost

"""list = ["python", "java", "swift", "javascript"]
computer = random.choice(list)
first_three = computer[:3]
missing = len(computer) - len(first_three)
dashes = "-" * missing

word = input(f"Guess the word {first_three}{dashes}: > ")

if word == computer:
    print("You survived!")
else:
    print("You lost!")"""

# 3. hráč má 8 pokusů na hádání písmen ve slově, slovo vybírá počítač ze zadaného seznamu,
# jeden pokus = - 1 život => přesně 8 pokusů na uhodnutí slova

"""comp_choice = ["python", "java", "swift", "javascript"]
computer = random.choice(comp_choice)
word = list("-" * len(computer))

attempts = 8

while attempts > 0:
    print()
    print("".join(word))

    letter = input("Input a letter: > ")

    found = False

    for i in range(len(computer)):
       if letter == computer[i]:
           word[i] = letter
           found = True

    if not found:
        print("That letter doesn't appear in the word.")

    attempts -= 1
print()

print("Thanks for playing!")"""

# 4. hráči se odečte "život" pouze když hádá špatně, nebo když zadá již jednou zadaný pokus
# celkem má 8 životů

"""comp_choice = ["python", "java", "swift", "javascript"]
computer = random.choice(comp_choice)
word = list("-" * len(computer))

attempts = 8
store_words = []

while attempts > 0:
    print()
    print("".join(word))

    letter = input("Input a letter: > ")

    if letter in store_words:
        attempts -= 1
        print("No improvements.")

    found = False

    for i in range(len(computer)):
        if letter == computer[i]:
            word[i] = letter
            store_words.append(letter)
            found = True

    if "-" not in word:
        print()
        print("You guessed the word!")
        print("You survived!")
        break


    if not found:
        attempts -= 1
        print("That letter doesn't appear in the word.")

if attempts == 0:
    print()
    print("You lost!")
"""


# 5. hráči se neodečítá život při hádání stejného (správného) písmene
# upřesnění znaku - může být zadán jen jeden znak, jen malá písmena abecedy

"""comp_choice = ["python", "java", "swift", "javascript"]
computer = random.choice(comp_choice)
word = list("-" * len(computer))

attempts = 8
store_words = []

while attempts > 0:
    print()
    print("".join(word))

    letter = input("Input a letter: > ")

    if letter in store_words:
        print("You've already guessed this letter.")

    if len(letter) != 1:
        print("Please, input a single letter.")
        continue

    if not letter.isalpha():
        print("Please, enter a lowercase letter from the English alphabet")
        continue

    elif letter.isupper():
        print("Please, enter a lowercase letter from the English alphabet.")
        continue

    found = False

    for i in range(len(computer)):
        if letter == computer[i]:
            word[i] = letter
            store_words.append(letter)
            found = True

    if "-" not in word:
        print()
        print(f'You guessed the word {"".join(word)}!')
        print("You survived!")
        break

    if not found:
        attempts -= 1
        print("That letter doesn't appear in the word.")

if attempts == 0:
    print()
    print("You lost!")"""

# 6. ve hře přibylo úvodní výběrové menu : play, result, exit

"""wins = 0
loses = 0

while True:
    user_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > ' )

    if user_choice == "play":
        comp_choice = ["python", "java", "swift", "javascript"]
        computer = random.choice(comp_choice)
        word = list("-" * len(computer))

        attempts = 8
        store_words = []

        while attempts > 0:
            print()
            print("".join(word))

            letter = input("Input a letter: > ")

            if letter in store_words:
                print("You've already guessed this letter.")

            elif len(letter) != 1:
                print("Please, input a single letter.")
                continue

            elif not letter.isalpha():
                print("Please, enter a lowercase letter from the English alphabet")
                continue

            elif letter.isupper():
                print("Please, enter a lowercase letter from the English alphabet.")
                continue

            store_words.append(letter)
            found = False

            for i in range(len(computer)):
                if letter == computer[i]:
                    word[i] = letter
                    found = True

            if "-" not in word:
                wins +=1
                print()
                print(f'You guessed the word {"".join(word)}!')
                print("You survived!")
                break

            if not found:
                attempts -= 1
                print("That letter doesn't appear in the word.")

        if attempts == 0:
            loses += 1
            print()
            print("You lost!")

    elif user_choice == "results":
        print(f"You won: {wins} times")
        print(f"You lost: {loses} times")

    elif user_choice == "exit":
        break"""
