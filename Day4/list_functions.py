# used to store data 
# built in data type which stores diff type of data inc float, int, strings etc

numbers= [1,2,3,6,7,90,34,0,89]

# length of the list: 
print(len(numbers))

# append element to a list i.e add one element at the end of the list
# numbers.append("hello")
print(numbers)

# sorting list : ascending order
numbers.sort()
print(numbers)

# sorting in descending order
numbers.sort(reverse=True)
print(numbers)

# reversing the list
numbers.reverse()
print(numbers)

numbers.insert(2, "fatema")
print(numbers)

# removing element from list i.e first occurrence of that element in the list

numbers.remove(0)

# pop used to delete number at particular index

numbers.pop(3)

print(numbers)