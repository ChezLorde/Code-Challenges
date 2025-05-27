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

num_cases = int(get_input())

for case_num in range(num_cases):
  sentence = get_input()
  detected = False

  for index in range(len(sentence)):
    if len(sentence) - index > 2 and sentence[index] == "r" and sentence[index + 1] == "e" and sentence[index + 2] == "d":
      detected = True
      print("red")
      break
    elif len(sentence) - index > 3 and sentence[index] == "b" and sentence[index + 1] == "l" and sentence[index + 2] == "u" and sentence[index + 3] == "e":
      detected = True
      print("blue")
      break

  if not detected:
    print("no color found")

  

