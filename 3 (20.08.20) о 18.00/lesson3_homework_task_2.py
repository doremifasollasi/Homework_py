# The second task. A four-digit natural number is specified. 
# Find the product of the digits of this number.
natural_number = 2847
indexed_natural_number = list(str(natural_number))
first_digit = int(indexed_natural_number[0])
second_digit = int(indexed_natural_number[1])
third_digit = int(indexed_natural_number[2])
fourth_digit = int(indexed_natural_number[3])
mult_natural_number = first_digit*second_digit*third_digit*fourth_digit
#print("The result of multiplication is equal to:", mult_natural_number)

#Sort the digits included in this number.
reverse_natural_number = indexed_natural_number[::-1]
#print("These are the digits of the number in reverse order:", reverse_natural_number)

#Sort the digits included in this number.
sorting_natural_number = sorted(indexed_natural_number)
#print("These are sorted numbers:",sorting_natural_number)