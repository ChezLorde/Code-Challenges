import sys
import string

def get_input():
  return sys.stdin.readline().rstrip()
  
def get_letter_values(a_value):
  a_index = a_value - 1
  letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
  end_cutoff = letters[26-a_index:26]
  beginning_cutoff = letters[0:26-a_index]
  letters = ["|"] + end_cutoff + beginning_cutoff
  return letters
  
get_letter_values(2)
  
num_cases = int(get_input())

for case_num in range(num_cases):
  data = get_input().split(" ")
  a_value = int(data[0])
  num_words = int(data[1])
  letter_values = get_letter_values(a_value)
  
  for word_num in range(num_words):
    word = get_input()
    word_value = 0
    for letter in word:
      letter_value = letter_values.index(letter.upper())
      word_value += letter_value
    
    if word_value == 100:
      print("WINNER " + str(a_value) + ": " + word)
      