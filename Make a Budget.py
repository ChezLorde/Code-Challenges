import sys

categories = {}

# Handles the transactions
def transact(category:str, deposit:str, amount:int) -> bool:

  balance = categories.get(category)
  
  # Determine if deposit or withdrawl
  if deposit == "+":
    categories.__setitem__(category, balance + amount)
    print("YES")
    return True
  
  else:
    # If the amount withdrawn is in the account, then remove that amount and return YES
    if amount <= balance:
      categories.__setitem__(category, balance - amount)
      print("YES")
      return True
    
    # Otherwise, do not transact and return NO
    else:
      print("NO")
      return False


num_cases = int(sys.stdin.readline().rstrip())

# For each test case:
for case_num in range(num_cases):
  # Get the number of categories and transactions
  budget_info = sys.stdin.readline().rstrip().split(" ")
  num_categories = int(budget_info[0])
  num_transactions = int(budget_info[1])

  # Setup the categories with the inputted name and starting balance
  for category_num in range(num_categories):
    categ_info = sys.stdin.readline().rstrip().split(" ")
    name = categ_info[0]
    starting_balance = int(categ_info[1])

    categories.__setitem__(name, starting_balance)

  # Do the transactions
  for transaction_num in range(num_transactions):
    transac_info = sys.stdin.readline().rstrip().split(" ")
    category = transac_info[0]
    deposit = transac_info[1]
    amount = int(transac_info[2])

    transact(category, deposit, amount)

  
