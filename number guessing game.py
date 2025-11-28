"""
first GitHub project, this is a number guessing game,
purely for learning how to navigate GitHub, untill
I am cofortable with making more complex projects.
"""
import random

def get_random_number(low: int, high: int) -> int:
  return random.randint(low, high)


def get_user_guess(low: int, high: int) -> int | None:
  """
  take user input and return it as an integer
  if it makes it through the input validation.
  """
  print()
  try:
    guess = input(f'guess a number between {low} and {high}: ')

    if guess.isdigit():
      guess = int(guess)
      # make sure the guess is within bounds
      if guess >= low and guess <= high:
        return guess
      else:
        print()
        print('invalid guess, try again.')
    else:
      print()
      print('invalid guess, try again.')
  except EOFError:
    print()
    print('EOFError, this program requires interactive input')
    return None

def check_user_guess(number: int, user_guess: int) -> bool:
  """
  check whether the guess was correct,
  higher, or lower, notify the user, and
  return True if the guess was correct.
  otherwise return False
  """
  if user_guess == number:
    # for clean output
    print()
    return True
  elif user_guess > number:
    print()
    print('lower')
    return False
  else:
    print()
    print('higher')
    return False

#================- main -=================#

def main():
  low = 1
  high = 100
  num_of_guesses = 6
  cur_guesses = 0
  random_number = get_random_number(low, high)

  while cur_guesses < num_of_guesses:
    user_guess = None
    # cycle untill user gives a valid input
    while user_guess is None:
      user_guess = get_user_guess(low, high)
    
    # win / loss system
    if check_user_guess(random_number, user_guess):
      print(f'you got it in {cur_guesses + 1} guesses!')
      return
    else:
      print(f'you have {num_of_guesses - cur_guesses - 1} guesses left.')
    
    cur_guesses += 1
  print(f'you ran out of guesses, the number was {random_number}')


if __name__ == '__main__':
  main()


