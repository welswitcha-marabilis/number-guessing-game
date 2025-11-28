"""
first GitHub project, this is a number guessing game,
purely for learning how to navigate GitHub, untill
I am cofortable with making more complex projects.
"""
import random

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
