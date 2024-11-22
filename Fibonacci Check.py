import sys
import string
import math

def is_fibonacci(f):
  
  # Define the start of the sequence. Neccessary in order to setup how the sequence will progress.
  sequence = [0, 0, 1, 1, 2]

  if f == 0 or f == 1 or f == 2:
    return True
  else:
    # If the term requested is beyond the scope of the initial list, compute the list until we get a value greater than or equal to the requested term.
    while sequence[len(sequence) - 1] < f:
      curr = sequence[len(sequence) - 1]
      prev = sequence[len(sequence) - 2]
      new_value = curr + prev
      sequence.append(new_value)

    # Return the correct term
    if sequence[len(sequence) - 1] == f:
      return True
    else:
      return False


# Get the number of test cases and iterate through
cases = int(sys.stdin.readline().rstrip())

for case_num in range(cases):

  # Get the value from the input
  term = int(sys.stdin.readline().rstrip())

  # Get the the result of the function
  is_fib = is_fibonacci(term)

  # Print the output
  to_print = str(is_fib).upper()
  print(to_print)

