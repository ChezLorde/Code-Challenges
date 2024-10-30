import sys
import string
import math

def diff(num1, num2):
  return abs(num2 - num1)

def get_rendering_grid(eye_x, eye_y):


  # Configuration
  grid_length = 20
  grid_height = 20

  # Set up the list
  grid = []

  # Determine value based on distance to eye positions
  for row_num in range(grid_height):
    row = []

    # Get the values for the row
    for column_num in range(grid_length):
      cell_value = 10

      x_dist = diff(eye_x, row_num)
      y_dist = diff(eye_y, column_num)

      # If the cell is the one being focused on, set resolution to 100%.
      if row_num == eye_x and column_num == eye_y:
        cell_value = 100
      
      # If the cell is within 1 cell of the focus cell, set resolution to 50%
      elif x_dist <= 1 and y_dist <= 1:
        cell_value = 50

      # If the cell is within 2 cells of the focus cell, set resolution to 25%
      elif x_dist <= 2 and y_dist <= 2:
        cell_value = 25

      # Add the cell to the row list
      row.append(cell_value)
    
    # Add the row to the grid list
    grid.append(row)

  # Return list
  return grid
    
# Get the number of test cases
test_cases = int(sys.stdin.readline().rstrip())

# Iterate through each test case
for case in range(test_cases):

  # Extract the coordinates from the inupt
  eye_coords = sys.stdin.readline().rstrip().split(" ")

  # Get the grid
  grid = get_rendering_grid(int(eye_coords[0]), int(eye_coords[1]))

  # Print the grid row by row
  for row in grid:
    row_output = ""
    for cell in row:
      row_output = row_output + str(cell) + " "
    print(row_output.rstrip())