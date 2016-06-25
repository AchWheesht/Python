import time
import math

def generate_primes(number_of_primes):
    prime_list = []
    number = 1
    list_length = 0
    while list_length < number_of_primes:
        if number % 5000 == 0: print("Basic analysed %d numbers (%d are prime)" % (number, list_length))
        number += 1
        is_prime = True
        for i in range(number):
            if i == 0 or i == 1: continue
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(number)
            list_length += 1
    print("Basic finished. Anaylsed %d numbers. %d are prime." % (number, list_length))
    return prime_list

def generate_primes_advanced(number_of_primes):
    prime_list = [2, 5]
    number = 1
    list_length = 0
    while list_length < number_of_primes:
        number += 1
        if number % 5000 == 0: print("Advanced analysed %d numbers (%d are prime)" % (number, list_length))
        if number % 2 == 0 or number % 5 == 0: continue
        is_prime = True
        number_range = list(range(int(number/2)))
        del number_range[0:2]
        for i in number_range:
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            list_length += 1
            prime_list.append(number)
    print("Advanced finished. Anaylsed %d numbers. %d are prime." % (number, list_length))
    return prime_list

def generate_primes_super_advanced(number_of_primes):
    prime_list = [2]
    number = 2
    list_length = 1
    previous_length = 0
    while list_length < number_of_primes:
        if number % 5000 == 0:
            #print("Super advanced analysed %d numbers (%d are prime) (%d new primes found)" % (number, list_length, (list_length - previous_length)))
            previous_length = list_length
        number += 1
        is_prime = True
        for prime in prime_list:
            sqrt_number = int(math.sqrt(number))
            if prime > sqrt_number: break
            if number % prime == 0:
                is_prime = False
                break
        if is_prime == True:
            list_length += 1
            prime_list.append(number)
    print("Super advanced finished. Anaylsed %d numbers. %d are prime." % (number, list_length))
    return prime_list

def time_function(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    #print(alist[:100])
    return (end - start)

while True:
    try:
        number_of_primes = int(input("How many primes?"))
    except ValueError:
        print("Need an integer!")
    else:
        if number_of_primes <= 0:
            number_of_primes = 1000
        else:
            break

# print(lista)
# print(listb)
#
# if lista == listb:
#     print("hooray")
# else:
#     print("boo")

# prime_list_time = time_function(generate_primes, number_of_primes)
# prime_list_advanced_time = time_function(generate_primes_advanced, number_of_primes)
#prime_list_super_advanced_time = time_function(generate_primes_super_advanced, number_of_primes)
# print("Basic prime generator took %.2f seconds" % prime_list_time)
# print("Advanced prime generator took %.2f seconds" % prime_list_advanced_time)
#print("Super advanced prime generator took %.2f seconds" % prime_list_super_advanced_time)

time_list = []
for i in range(10):
    recorded_time = time_function(generate_primes_super_advanced, 10000)
    time_list.append(recorded_time)

print(time_list)

total = 0
for i in time_list:
    total += i

print(total)
average = total / 10.0

print("Average Time: %.10f" % average)
#Super Advanced Prime Generator Theory

#1. All non-prime numbers can factor into primes.
#2. All non-prime factors for non-prime numbers can factor into primes
#3. Therefore, we only need to check prime factors

#4. A number cannot be factored by a number greater than its half
#5. There is only one possible factor greater than its third (2)
#6. There is only one *prime* factor greater than its quarter (2)
#7. A second possible prime factor occurs only at it's fifth (5)
#8. And a third occurs at its seventh (7)

#9. We can take this into account when finding non-prime numbers by always finding the smaller prime factor first.
#10. But we clearly do not need to check all possible factors if the number is prime
#11. As we can rule out all numbers above half if it does not divide by two etc.
#12. The largest possible smallest factor is the square root of the number in question
#13. So we do not need to check any number above the square root of the number in question, rounded down.
