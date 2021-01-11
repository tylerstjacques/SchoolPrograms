def read_in_answer(filename):
    """ Read in and return a single number from a file, the answer to the guessing game """
    with open(filename) as fp:
        answer = int(fp.readline())
    return answer


def get_a_guess():
    """ prompt the user for a guess and read it in and return it"""
    guess = int(input('Make a guess: '))
    return guess


def evaluate_a_guess(guess, answer):
    """
    Return true if guess equals the answer, false otherwise.
    Also print out "right!" if the guess is correct,
    "too low!" if guess is too low,
    or "too high!" if guess is too high.
    """
    if guess == answer:
        print('right!')
    elif guess < answer:
        print('too low!')
    else:
        print('too high!')


