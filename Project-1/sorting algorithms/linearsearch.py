def linear_search(num_list,element_to_find):
    for index, element in enumerate(num_list):
        if element == element_to_find:
            return index


    return -1

number_list = [int(x) for x in input("Enter the array elements:").split()]
num_to_find = int(input("enter the number to find:"))
index = linear_search(number_list,num_to_find)
print(f"element found at index {index} using linear search ")
