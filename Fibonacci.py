import sys
import string
import math

def fibonacci(n):
  
  # Define the start of the sequence. Neccessary in order to setup how the sequence will progress.
  sequence = [0, 0, 1, 1, 2]

  # If the term requested is beyond the scope of the initial list, compute the list up to the correct term
  while len(sequence) - 1 < n:
    curr = sequence[len(sequence) - 1]
    prev = sequence[len(sequence) - 2]
    new_value = curr + prev
    sequence.append(new_value)

  # Return the correct term
  return sequence[n]

# Get the number of test cases and iterate through
cases = int(sys.stdin.readline().rstrip())

for case_num in range(cases):

  # Get the position from the input
  position = int(sys.stdin.readline().rstrip())

  # Get the term from the function
  term = fibonacci(position)

  # Print the output
  to_print = str(position) + " = " + str(term)
  print(to_print)