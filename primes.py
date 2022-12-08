"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def get_prime_after(current):
    is_prime = False;
    
    while(is_prime == False):
        current = current + 1
        caught_divisible = False

        for x in range(2, current):
            if current % x == 0:
                caught_divisible = True
                break
        
        if caught_divisible == False:
            is_prime = True

    return current



def primes(number_of_primes):
    if(number_of_primes <= 0):
        raise ValueError(f"number={number_of_primes} should have been a positive number!")

    list = [2]

    while(len(list) != number_of_primes):
        list.append(get_prime_after(list[len(list)-1]))

    return list
