import sys

def get_input() -> str:
  return sys.stdin.readline().rstrip()

num_cases = int(get_input())

for case_num in range(num_cases):
  limit = int(get_input())

  remain = list(range(2, limit + 1))
  primes = []

  # Keep going through the remaining list, checking the first number, until the list is empty
  while len(remain) > 0:

    # Add number to primes + take it out of the list
    prime = remain[0]
    primes.append(prime)
    remain.remove(prime)

    # Set up number of removed composites
    removed_composites = 0

    # Go through list
    for num in remain:
      # If it is a multiple of the number, then remove it and add to removed_composites
      if num % prime == 0:
        remain.remove(num)
        removed_composites += 1

    # Print the message of the removed composite sets (if there are any)
    if removed_composites > 0:
      print("Prime " + str(prime) + " Composite Set Size: " + str(removed_composites))

  # Print the list of primes
  message = "{"

  for item in primes:
    message += str(item) + ","
  
  message = message.removesuffix(",") + "}"
  print(message)

  
