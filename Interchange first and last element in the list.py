# Initialize an empty list called interchange_f_l_list
interchange_f_l_list = list()

# Ask the user to enter the number of elements they want in the list and convert it to an integer
n = int(input("Enter number of elements: "))

# Use a loop to take input 'n' times from the user and append each element to the list
for i in range(n):
    m = input("Enter Element: ")
    interchange_f_l_list.append(m)

# Print the list after taking input from the user
print("List after input:", interchange_f_l_list)

# Interchange the first and last elements of the list using tuple unpacking
interchange_f_l_list[0], interchange_f_l_list[-1] = interchange_f_l_list[-1], interchange_f_l_list[0]

# Print the list after interchanging the first and last elements
print("List after interchange:", interchange_f_l_list)
