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

def is_int(num):
  if int(num) == num:
    return True
  else:
    return False

def coprimes(num1:int, num2:int) -> bool:
  coprime = True

  # Make sure num2 is the larger number; otherwise swap them
  if num1 > num2:
    num1, num2 = num2, num1
  
  # Divide by every integer up to the largest number
  for div in range(2, num2):
    # If, when dividing, both numbers return integer values, then they are not coprime.
    if is_int(num2 / div):
      if is_int(num1 / div):
        coprime = False
        break
  
  return coprime

num_cases = int(get_input())

for case_num in range(num_cases):
  number = get_input().split(")")
  a = int(number[0].removeprefix("("))
  remaining_nums = number[1].split("-")
  b = int(remaining_nums[0])
  c = int(remaining_nums[1])

  if coprimes(a,b) and coprimes(a,c) and coprimes(b,c):
    print("TRUE")
  else:
    print("FALSE")
