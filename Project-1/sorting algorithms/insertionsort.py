def insertion_sort(numbers):
    for i in range (1,len(numbers)):
        a = numbers[i]
        j=i-1
        while j>=0 and a <numbers[j]:
            numbers[j+1]=numbers[j]
            j = j-1
        numbers[j+1]=a

num_list = [int(x) for x in input("enter the number list: ").split()]
sorted_list= insertion_sort(num_list)
print(num_list)
