
input_file_name = "1_Input.txt"
input_file = open(input_file_name, "r")

list1 = []
list2 = []

# Inserts an integer into a list in the correct position
def sorted_insert(list:list, value:int) -> int:
  index = 0

  # Go through until you find a value in the list that is not less than the one we are trying to insert.
  while index < len(list) and list[index] < value:
    index += 1
  
  # Add the value
  list.insert(index, value)

  return index

# Break each line into the left and right values and put them in their respective lists
for line in input_file:
  values = line.split("   ")
  sorted_insert(list1, int(values[0]))
  sorted_insert(list2, int(values[1]))

# Compare the differences of each sorted list value and add it to the total
def total_differences():
  total_difference = 0
  for index in range(len(list1)):
    value1 = list1[index]
    value2 = list2[index]
    difference = abs(value1 - value2)
    total_difference += difference

  print(total_difference)
  return total_difference

# Similarity Scores: How many times one thing from the first list appears in the seconds times its value.
def similarity_score():
  total_score = 0
  for i in range(len(list1)):
    num_copies = 0
    for j in range(len(list2)):
      if list1[i] == list2[j]:
        num_copies += 1
    total_score += num_copies * list1[i]
  
  print(total_score)
  return total_score

similarity_score()