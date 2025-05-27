import sys

def get_input() -> str:
  return sys.stdin.readline().rstrip()

num_cases = int(get_input())

for case_num in range(num_cases):
  message = ""

  num_lines = int(get_input())

  # Go through each line and add the letter at the specified index to the end of the message string
  for line_num in range(num_lines):
    line_data = get_input().split("|")
    words = line_data[0]
    index = int(line_data[1])

    message += words[index]

  print(message)

