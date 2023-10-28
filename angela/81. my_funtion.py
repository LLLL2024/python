import math
def paint_calc(height, width,cover):
    area =  height * width
    num_of_area =  math.ceil(area / cover)
    print(f"{num_of_area}")
test_h = int(input("height of wall:"))
test_w = int(input("width of with"))
coverage = 5
paint_calc(height=test_h, width=test_w, cover = coverage)