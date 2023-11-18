# Write a Python program to count the number of even and odd numbers from a series of numbers.

my_list = (1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20)

def odd_even(my_list):
    even = 0
    odd = 1
    for i in my_list:
        if i % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
            
    print(my_list, f"Number of even numbers: {even}, Number of odd numbers: {odd}")

odd_even(my_list)