import sys
import decimal

def get_input() -> str:
  return sys.stdin.readline().rstrip()

num_cases = int(get_input())

for case_num in range(num_cases):
  num_items = int(get_input())
  projected_costs = get_input().split(" ")
  actual_costs = get_input().split(" ")
  cost_variances = []

  # Calculate the cost variance for each line item
  for index in range(num_items):
    proj = float(projected_costs[index])
    real = float(actual_costs[index])
    cost_var = real - proj
    cost_variances.append(cost_var)

  # Calculate the average variance
  avg_variance = decimal.Decimal(sum(cost_variances) / num_items, decimal.BasicContext).quantize(decimal.Decimal("1.00"), rounding=decimal.ROUND_HALF_UP)

  '''
  # Take out negative zero values
  if avg_variance == 0.0:
    avg_variance = 0.0'''

  '''
  # Determine whether to add a trailing zero
  extra_zeroes = ''
  after_decimal = str(avg_variance).split(".")[1]
  if len(after_decimal) < 2:
    extra_zeroes += '0'''

  # Print the result
  print(str(avg_variance))

  
  
