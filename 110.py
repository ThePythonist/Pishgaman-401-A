from random import choice, randint

number = randint(0, 10)
chance = 5

while chance > 0:
    print("You have", chance, "chances left")
    print()
    guess = int(input("Guess the number : "))
    if 0 <= guess <= 10:
        if guess == number:
            print("You won!")
            break
        elif guess > number:
            print("Try smaller than", guess)
            print()
        else:
            print("Try bigger than", guess)
            print()

        chance -= 1
    else:
        print("Entry must be 0...10")
        print()

if chance == 0:
    print("You lose! The number was", number)
