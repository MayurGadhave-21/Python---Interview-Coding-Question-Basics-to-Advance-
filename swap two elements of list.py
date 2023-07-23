# Create an empty list called swap_element_of_list
swap_element_of_list = []

# Ask the user to enter the number of elements they want in the list and convert it to an integer
num_elements = int(input("Enter number of elements in the list: "))

# Use a loop to take input 'num_elements' times from the user and append each element to the list
for i in range(num_elements):
    element = int(input("Enter element: "))
    swap_element_of_list.append(element)

# Print the list after taking input from the user
print("List:", swap_element_of_list)

# Ask the user to enter the first index and the last index to swap
first_index = int(input("Enter first index to swap: "))
last_index = int(input("Enter another index to swap: "))

# Check if the entered indices are valid (within the range of the list)
if first_index < len(swap_element_of_list) and last_index < len(swap_element_of_list):

    # Swap the elements at the specified indices using tuple unpacking
    swap_element_of_list[first_index], swap_element_of_list[last_index] = swap_element_of_list[last_index], swap_element_of_list[first_index]

    # Print the list after swapping the elements
    print("List after swapping:", swap_element_of_list)
else:
    # If the indices are out of bound, print an error message
    print("Error: Index out of bound")
