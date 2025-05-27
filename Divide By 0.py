import sys

def divide(dividend, divisor) -> float:
  flo_dend = 0.0
  flo_isor = 0.0
  result = 0.0

  # Check dividend
  try:
    flo_dend = float(dividend)

     # Check divisor
    try:
      flo_isor = float(divisor)

      # Check division
      try:
        result = flo_dend / flo_isor
        print(round(result, 1))

      except ZeroDivisionError:
        print("Divide By Zero")

    except ValueError:
      print("Invalid Divisor")

  except ValueError:
    print("Invalid Dividend")


testcases = int(sys.stdin.readline().rstrip())


for casenum in range(testcases):
  inputs = sys.stdin.readline().rstrip().split(" ")
  divide(inputs[0], inputs[1])

