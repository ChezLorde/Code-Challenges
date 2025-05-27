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

num_cases = int(get_input())

for case_num in range(num_cases):
  data = get_input().split(" ")
  density = float(data[0])
  volume = float(data[1])

  mass = decimal_round(density * volume, 2)
  print(mass)

