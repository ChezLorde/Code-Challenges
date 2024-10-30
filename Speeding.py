import sys
import math
import string

def is_speeding(speed, birthday):
  
  # Set the amount over which the officer will look away if it is your birthday
  if birthday == "true":
    break_amount = 5
  else:
    break_amount = 0
    
  if speed - break_amount <= 60:
    return "no ticket"
  elif speed - break_amount <= 80:
    return "small ticket"
  else:
    return "big ticket"
    
cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
  problem_input = sys.stdin.readline().rstrip() 
  input = problem_input.split(' ') #separate by space
  first_argument = int(input[0])
  second_argument = input[1]

  print(is_speeding(first_argument,second_argument))


    
    
    
  
    