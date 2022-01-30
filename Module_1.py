
# TASK 1 - create list of 100 random numbers from 0 to 1000
# randint from random module is imported in order to generate random numbers
# need only one function from module random, not all of them.
from random import randint
''' create 'random_list' - list of random integer values
for loop is used in order to generate 100 numbers.
randint(0, 1000) is used for generation of random number from 0 to 1000.'''
random_list = [randint(0, 1000) for i in range(100)]
# print the result Output - random list
print('Task1\n  Random list:', random_list)

# We can use sample() method if we need to create list with a randomly unique numbers
# a = random.sample(range(0, 1000), 100)




# TASK 2 - sort list from min to max (without using sort())
# Bubble sort algorithm is used to solve the task
# It needs len(random_list)-1 iterations for each value. len(random_list) is 'random_list' lengths
for i in range(len(random_list)-1):
    # how many times to perform comparison for each element: depends on its position,
    # >> length of the list - current position, additionally subtract 1 if we use length in iterations
    # because indexing starts from 0
    for j in range(len(random_list) - i - 1):
        # Condition that checks whether left-placed element more than right-placed element
        # if next element is smaller than current
        # random_list[j] - current element, random_list[j+1] - the following element.
        if random_list[j+1] < random_list[j]:
            # reassign them between each other, so the greater will be following smaller number
            # in case condition is True elements will be swapped.
            random_list[j], random_list[j+1] = random_list[j+1], random_list[j]
# print the result Output - sort list
print('\nTask2\n  Sort list: ' , random_list)


# TASK 3 -  calculate average for even and odd numbers
# create lists with even and odd numbers
even_numbers = [number for number in random_list if number % 2 == 0]
odd_numbers = [number for number in random_list if number % 2 != 0]
print ('\nTask3\n Even numbers: ', even_numbers)
print (' Odd numbers: ', odd_numbers)



# TASK 4 - print both average result in console
print('\nTask4')
# if the list with even numbers will be empty [] (length == 0 )
if len(even_numbers) == 0:
    print('Can not count average, there are no even numbers.')
# if the list with even numbers will be NOT empty (length > 0), then we can count avg value 'even_avg'
else:
    # count average number from even numbers list 'even_avg' (avg=sum/count)
    even_avg = sum(even_numbers) / len(even_numbers)
    # print even_avg and round it with 2 numbers after ','
    print('Average number from even numbers list:', round(even_avg, 2))


# if the list with odd numbers will be empty [] (length == 0 )
if len(odd_numbers) == 0:
       print('Can not count average, there are no odd numbers.')
# if the list with odd numbers will be NOT empty (length > 0), then we can count avg value 'odd_avg'
else:
    # count average number from odd numbers list 'odd_avg' (avg=sum/count)
    odd_avg = sum(odd_numbers) / len(odd_numbers)
    # print odd_avg and round it with 2 numbers after ','
    print('Average number from odd numbers list:', round(odd_avg, 2))




