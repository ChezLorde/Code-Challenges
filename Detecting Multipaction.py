import sys

def get_input() -> str:
  return sys.stdin.readline().rstrip()

# Determines if there is a multipaction risk based on the level of activity
def mult_risk(level:float) -> bool:
  if level >= .6 and level <= .85:
    return True
  else:
    return False

num_cases = int(get_input())

for case_num in range(num_cases):
  # Extract data from channels
  null = get_input().split(" ")
  third = get_input().split(" ")

  multipaction_indices = []

  # If both channels are at risk, then label the time index and add it to the list
  for index in range(len(null)):
    if mult_risk(float(null[index])) and mult_risk(float(third[index])):
      multipaction_indices.append(index)
  
  # Print the number of multipaction indices and time indexes detected
  if len(multipaction_indices) == 0:
    print("No multipaction events detected.")
  elif len(multipaction_indices) == 1:
    print("A multipaction event was detected at time index " + str(multipaction_indices[0]) + ".")
  else:
    indices = ""
    for value in multipaction_indices:
      indices = indices + " " + str(value)
    print(str(len(multipaction_indices)) + " multipaction events were detected at time indices:" + indices + ".")
