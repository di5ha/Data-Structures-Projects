def binary_search(num_list,element_to_find):
    left_index =0
    right_index = len(num_list)-1
    mid_index =0

    while left_index <= right_index:
        mid_index=(left_index+right_index)//2
        mid_num = num_list[mid_index]
        if mid_num==  element_to_find:
            return mid_index
        if mid_num< element_to_find:
            left_index=mid_index+1
        else:
            right_index = mid_index-1
    return -1

number_list = [int(x) for x in input("enter the number list:").split()]
num_to_find= int(input("enter the number to find:"))
index = binary_search(number_list,num_to_find)
print(f"the element is at index {index}")