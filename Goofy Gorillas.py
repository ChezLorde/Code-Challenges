import sys

def should_alert(gor1_smiling, gor2_smiling):
  # Both are smiling OR both are frowning means they have the same facial expression.
  if gor1_smiling == gor2_smiling:
    return "true"
  else:
    return "false"

# Output block
testcases = int(sys.stdin.readline().rstrip())
for casenum in range(testcases):
  inputs = sys.stdin.readline().rstrip().split(" ")
  gor1_smiling = inputs[0]
  gor2_smiling = inputs[1]

  print(should_alert(gor1_smiling, gor2_smiling))