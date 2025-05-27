import sys
import datetime
from decimal import *

class file:
  def __init__(self, name:str, score:float, size:int):
    self.name = name
    self.score = score
    self.size = size

def get_input() -> str:
  return sys.stdin.readline().rstrip()


def datetime_days(day:int, month:int, year:int):
  today = datetime.date(2019, 4, 27)
  selected_date = datetime.date(year, month, day)
  days = (today - selected_date).days
  print("Datetime: "+str(days))

def get_days(day:int, month:int, year:int):
  today = [27, 4, 2019]

  # Calculate number of years ago
  num_years = abs(today[2] - year)

  # Calculate number of days ago minus yeap days

  # Create a list of every day of the year with corresponding months
  month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
  calendar = []
  month_start_indexes = [None]

  for index in range(len(month_lengths)):
    month_start_indexes.append(len(calendar)) #< - So we know where to start looking for each month

    for i in range(month_lengths[index]):
      calendar.append(index + 1)

  # Find the indexes of today and the requested day/month. Find the index of the first of the month and add the number of days.
  today_index = month_start_indexes[today[1]] + today[0] - 1
  requested_index = month_start_indexes[month] + day - 1

  num_days = today_index - requested_index

  # Finds the number of leap days between two years
  num_leap_days = 0
  for year in range(year, today[2], 1):
    if year % 4 == 0:
      if year % 100 == 0:
        if year % 400 == 0:
          num_leap_days += 1
      else:
        num_leap_days += 1

  # If the file date does not go back to Leap Day, remove a Leap Day.  
  if month > 2 and num_leap_days > 0:
    num_leap_days -= 1

  # Return the number of days
  days = 365 * num_years + num_days + num_leap_days
  #print("Total: " + str(days) + " Years: " + str(num_years) +" Days: " + str(num_days) + " Leap Days: " + str(num_leap_days))
  return days

def calculate_score(day:int, month:int, year:int, AM:bool, file_size:int) -> Decimal:
  # Get the number of days from the DateTime module
  #today = datetime.date(2019, 4, 27)
  #selected_date = datetime.date(year, month, day)
  #days = (today - selected_date).days
  days = get_days(day, month, year)

  # Determine the morning/afternoon
  if not AM:
    days -= 0.5
  
  # Multiply by the filesize to determine the score
  score = file_size * Decimal(days, BasicContext)

  # Round the score to three decimal places and return it.
  return Decimal(score, BasicContext).quantize(Decimal("1.000"), rounding=ROUND_HALF_UP)

#======================================================================================================================================

num_cases = int(get_input())

for case_num in range(num_cases):
  drive_data = get_input().split(" ")
  num_files = int(drive_data[0])
  drive_size = Decimal(drive_data[1], BasicContext) * 1000 

  # Order the files on the chopping block in terms of score
  files = []

  for file_num in range(num_files):
    # Extract the data from the message and calculate score
    file_data = get_input().split(" ")
    date = file_data[0].split("/")
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])
    am = (file_data[2] == "AM")
    size = Decimal(file_data[3], BasicContext) / 1000 #<- Turn to megabytes
    name = file_data[4]
    score = calculate_score(day, month, year, am, size)

    new_file = file(name, score, size)

    # Order the file in the list
    index = 0
    if len(files) > 0:
      for index in range(len(files)):
        if files[index].score < score:
          break
    files.insert(index, new_file)

  # Remove the files
  amount_removed = 0
  index = 0

  while amount_removed < (drive_size / 4):
    # Choose the file with the next-highest score
    rm_file = files[index]

    # "Remove" the file and index forward
    print(rm_file.name + " " + str(rm_file.score).rstrip())
    amount_removed += rm_file.size
    index += 1


