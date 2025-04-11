# This entrypoint file to be used in development. Start by reading README.md
from mean_var_std import calculate
 
# Make sure this list has exactly 9 numbers
input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
 
# Call the function with the list
result = calculate(input_list)
 
# Print the result
print(result)