def distance(x1, y1, x2, y2):
    '''Find The Distance Between Two Points.
    The funcion givens two ordered pairs and 
    calculates the distance between them, 
    rounds to two decimal places.'''
    return round(((x2 - x1)**2 + (y2 - y1)**2) ** 0.5, 2)

print(distance(2,1,4,5)) #4.47