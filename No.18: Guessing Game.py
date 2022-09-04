secret_num = 77

guess = int(input("Please Guess an Integer Number between 1 and 100: "))

count = 0
limit = 5

while guess != secret_num:
    if guess > secret_num:
        print("Too big!")
        count += 1
        guess = int(input("Guess Again: "))
    elif guess < secret_num:
        print("Too small")
        count += 1
        guess = int(input("Guess Again: "))
    if count >= 5:
        print("You lose!")
        break

if guess == secret_num:
    print("Exactly")