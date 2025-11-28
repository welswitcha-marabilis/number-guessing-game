







def get_random_number(low: int, high: int) -> int:
  return random.randint(low, high)


def get_user_guess(low: int, high: int) -> int | None:
  """
  take user input and return it as an integer
  if it makes it through the input validation.
  """
  print()
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
