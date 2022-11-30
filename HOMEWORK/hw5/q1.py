n = float(input("Enter a number to guess for square root: "))

init_guess = n/2
init_loop = 5

for i in range(3):
    guess = init_guess
    temp = 0
    for j in range(i + init_loop):
        temp = (guess + n/guess)/2
        guess = temp
    print("After {} iterations, the guess is {:.3f}".format(i + init_loop, guess))
