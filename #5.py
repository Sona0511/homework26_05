#A number is called a perfect number if it is equal to the sum of all of its divisors, not including the number itself.
#For instance, 6 is a perfect because the divisor of 6 are 1,2,3,6 and 6=1+2+3. As another example 28 is a perfect number because its divisors are 1,2,4,7,14,28 and 28=1+2+14+7
#However 15 is not a perfect number because its diviors are 1,3,5,15 and 15!=1+3+5.
#Write a program that finds all of the perfect numbers taht are less than 10,000.
def perfect_number(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors) == num

perfect_numbers = []
for num in range(1, 10000):
    if perfect_number(num):
        perfect_numbers.append(num)

print("Perfect numbers for the range of (1, 10000) are:")
for num in perfect_numbers:
    print(num)
