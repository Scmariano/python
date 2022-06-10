# 1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

from hashlib import new


def num_list(num):
    countdown = []
    
    for i in range (num, -1, -1):
        countdown.append(i)
    return countdown
    
    
print(num_list(5))

# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def num_list(num):
    print(num[0])
    return num[1]
print(num_list ([1,2]))

# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def add_list(list):
    print(list[0])
    return len(list)

print(add_list([20, 42, 1232, 54, 3, 12]))

#4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def values_greater_than_second(list):
    new_list = []
    if len(list) < 2:
        return False

    for i in list:  
        if i > list[2]:
            new_list.append(i)
    print(len(new_list))
    return new_list


print(values_greater_than_second([5,6,3,2,1,4]))
print (values_greater_than_second([]))

# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def length_and_value (size, value):
    new_list = []

    for i in range (size):
        new_list.append(value)
    return new_list

print(length_and_value(7,7))   
