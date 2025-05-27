import sys
import math
import string

def get_input() -> str:
  return sys.stdin.readline().rstrip()

num_cases = int(get_input())

for case_num in range(num_cases):
  length = int(get_input())
  data_stream = get_input()

  i = 0

  # Iterate through until there is not enough for a message.
  while i < length - 5:
    indicator = data_stream[i:i+3]
    reverse_indicator = "".join(reversed(indicator))

    index = data_stream.find(reverse_indicator)

    if index != -1:
      str_2 = data_stream[i+3:index]
      message = ""
      skip = True

      for char in str_2:
        if skip:
          skip = False
        else:
          message += char
    
      else:
        message += char
    
    if message != "":
      print(message)
    i = index + 3
  else:
    i += 1
    

# See if character is the next character in the alphabet
    # If we are reading a hidden message, then see if the next 3 are the reverse of the start key
    # If so: add to length of characters read.
    # If not: save next 3 as key-Variable. Iterate through until we find the reverse. 
        # Set a boolean so we can begin collecting the intervening amount as a hidden message
    