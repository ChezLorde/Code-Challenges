import sys
import math
import string
from decimal import *

def get_input() -> str:
  return sys.stdin.readline().rstrip()

def decimal_round(number:float, digits:int) -> Decimal:
  quant = "1."
  for i in range(digits):
    quant += "0"
  return Decimal(number, BasicContext).quantize(Decimal(quant), rounding=ROUND_HALF_UP)

def concat_list(list1:list, separator:string) -> str:
  message = ""
  for item in list1:
    message = message + str(item) + separator
  message = message.removesuffix(separator)
  return message

def next_index(curr, size):
  curr += 1
  curr %= size
  return curr

def num_characters(list1):
  num_chars = 0

  for item in list1:
    if item != "":
      num_chars += 1

  return num_chars

def is_int(num):
  if int(num) == num:
    return True
  else:
    return False

num_cases = int(get_input())

for case_num in range(num_cases):
  info = get_input().split(" ")
  num_commands = int(info[0])
  size = int(info[1])

  buffer = [""] * size
  pointer = 0
  
  for comm_num in range(num_commands):
    command = get_input().split(" ", 1)

    if command[0] == "ADD":
      to_add = command[1].split(" ")
      index = pointer
      
      # Move the index until we find the first blank space; otherwise, if we find the pointer again
      while buffer[index] != "":
        index = next_index(index, size) #<- Return index back to start if exceeds limit
        if index == pointer:
          break

      # Add the characters
      while len(to_add) > 0:
        # See if we are overwriting something; if we are, move the pointer forward
        if buffer[index] != "":
          pointer = next_index(pointer, size)

        # Set the index to the character
        buffer[index] = to_add[0]

        # Remove the character from the list
        to_add.remove(to_add[0])

        # Move the index forward
        index = next_index(index, size)

    elif command[0] == "CONSUME":
      to_consume = int(command[1])
      
      # While there are still spots to consume, consume the current spot and kick the pointer forward
      while to_consume > 0:
        buffer[pointer] = ""
        to_consume -= 1
        pointer = next_index(pointer, size)

    elif command[0] == "SHOW":
      #print(buffer)

      num_chars = num_characters(buffer)
      
      # If empty, print(empty)
      if num_chars == 0:
        print("Empty")
      else:
        total_dist = 0
        end = pointer
     
        while buffer[next_index(end, size)] != "" and next_index(end,size) != pointer:
          end = next_index(end, size)
          total_dist += 1
        
        # Find the midpoint between the pointer and the end
        midpoint = (pointer + total_dist / 2) % size
        
        # If odd, print the midpoint character between the pointer and the end
        if is_int(midpoint):
          print(buffer[int(midpoint)])
        # If even, print() the two characters on either side of the midpoint character
        else:
          print(buffer[int(midpoint - 0.5) % size] + " " + buffer[int(midpoint + 0.5) % size])


