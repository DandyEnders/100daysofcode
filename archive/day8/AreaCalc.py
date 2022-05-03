import math

def paint_calc(height, width, cover):
  area = test_h * test_w
  n_cans = math.ceil(area / cover)
  return n_cans
  
test_h = int(input("Height of wall: "))
test_w = int(input("Weidth of wall: "))
coverage = 5
n_cans = paint_calc(height=test_h, width=test_w, cover=coverage)

print(f"You need {n_cans} paint cans.")