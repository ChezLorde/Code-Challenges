import sys
import string
import math

def get_distance(x1, y1, x2, y2):
  dist_x = abs(x2 - x1)
  dist_y = abs(y2 - y1)
  
  distance = math.sqrt(dist_x ** 2 + dist_y ** 2)
  
  return distance
  
def organize_list(asteroid_positions):
  ordered_list = []
  
  for position in asteroid_positions:
    distance = get_distance(int(position[0]), int(position[1]), 0, 0)
    fits_in_list = False
    
    if len(ordered_list) > 0:
      for index in range(len(ordered_list)):
        if get_distance(int(ordered_list[index][0]), int(ordered_list[index][1]), 0, 0) > distance:
          ordered_list.insert(index, position)
          fits_in_list = True
          break
    
    if not fits_in_list:
      ordered_list.append(position)
      
  return ordered_list
  

  
cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
  num_asteroids = int(sys.stdin.readline().rstrip())
  
  asteroids = []
  
  for asteroid in range(num_asteroids):
    problem_input = sys.stdin.readline().rstrip()
    coordinates = problem_input.split(" ")
    asteroids.append(coordinates)
    
  asteroids = organize_list(asteroids)
  
  for asteroid in asteroids:
    print(str(asteroid[0]) + " " + str(asteroid[1]))
    
    
    
    
    

  
