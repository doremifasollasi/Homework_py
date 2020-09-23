def zero_fuel(distance_to_pump, mpg, fuel_left):
    """Function returns true (1 in Prolog) if it is possible 
    and false (0 in Prolog) if not."""
    if distance_to_pump/mpg > fuel_left:
        return False
    else:
        return True

print(zero_fuel(160,8,25))