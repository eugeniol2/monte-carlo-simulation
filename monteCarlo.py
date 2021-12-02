import math
import random

def upperSideFunction(x):        
        return x**2 + 0.5

def lowerSideFunction(x):
        return x**2

count = 0.0
in_area= 0.0

Xstart_value = 0
Xend_value = 1

Ystart_value = 0
Yend_value = 1

Yarea_value = Xend_value - Xstart_value
Xarea_value = Yend_value - Ystart_value

while count < 1000000:
        x_coord = random.uniform(Xstart_value,Xend_value)
        y_coord = random.uniform(Ystart_value,Yend_value)
        
        if y_coord < upperSideFunction(x_coord) and y_coord > lowerSideFunction(x_coord):
                
                in_area += 1
                
        count+= 1

area_box = Yarea_value * Xarea_value
print(in_area)
print(count)
print('Probabilidade do ponto cair no rio: {}%'.format((in_area/count)*100))
print('area do cubo:{}' .format(area_box))

print('area do rio: {}'.format((area_box * (in_area/count))))
