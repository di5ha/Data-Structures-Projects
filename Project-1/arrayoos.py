
def insert_arr(arr,index,element):
    arr.insert(index,element)

def del_arr(arr,index):
    if 0<= index<= len(arr):
        arr.pop(index)
    else:
        print("index not found")

def search_arr(arr,element):
    if element in arr:
        return arr.index(element)
    else:
        print("Element not found")

def update_arr(arr,index,new_element):
    if 0<= index <= len(arr):
        arr[index]=new_element
    else:
        print("index not found")

array = [int(x) for x in input("Enter the array elements:").split()]
print("original array:",array)

index_to_insert = int(input("enter the index to insert:"))
element_to_insert=int(input("enter the element to be inserted:"))
insert_arr(array,index_to_insert,element_to_insert)
print("after insertion",array)

index_to_delete=int(input("enter index to delete"))
del_arr(array,index_to_delete)
print("after deletion:",array)

element_to_search = int(input("insert element to search:"))
search_arr(array,element_to_search)


index_to_update =int(input("index to update:"))
element_to_update= int(input("element to be inserted:"))
update_arr(array,index_to_update,element_to_update)
print("after updating:")



