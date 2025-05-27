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

def hex_to_int(hex):
  return int(hex, base=16)

num_cases = int(get_input())

for case_num in range(num_cases):
  

    
