# python program to calculate Euler's Totient Function

# Function to return gcd of a and b
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)


# A simple method to evaluate Euler Totient Function
def phi(n):
    result = 1;
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result += 1
    return result


def mod(n, m):
    return n % m

def eucledian(e, phi_n):
    i = 0
    while(1):
        if ((1 + i * phi_n) % e == 0):
            d = (1 + i * phi_n) / e
            break
        i += 1
    return d

# Driver program to test above function
n = 35 # put the value of n here
phi_n = phi(n)

print(f'phi of {n} = {phi_n}')
print(f'd = {eucledian(5, phi_n)}')