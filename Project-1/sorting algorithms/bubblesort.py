def bubble_sort(numbers):
    size = len(numbers)
    for j in range(size-1):
        for i in range(size-1-j):
            if numbers[i] > numbers[i+1]:
                x = numbers[i]
                numbers[i]=numbers[i+1]
                numbers[i+1]=x
    return numbers
number_list =[int(x) for x in input("enter the number list:").split()]
num = bubble_sort(number_list)
print(f"The sorted list is :{num}")