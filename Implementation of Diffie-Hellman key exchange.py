import random

def mod_exp(a, b, m):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result

def generate_prime():
    while True:
        num = random.randint(2**10, 2**12)
        if is_prime(num):
            return num

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def diffie_hellman():
    p = generate_prime()
    g = random.randint(2, p - 1)
    a = random.randint(2, p - 2)
    b = random.randint(2, p - 2)
    A = mod_exp(g, a, p)
    print("Xa: ",A)
    B = mod_exp(g, b, p)
    print("Xb: ",B)
    secret_A = mod_exp(B, a, p)
    secret_B = mod_exp(A, b, p)
    return secret_A, secret_B

shared_secret_A, shared_secret_B = diffie_hellman()
print("Shared secret A:", shared_secret_A)
print("Shared secret B:", shared_secret_B)
if shared_secret_A == shared_secret_B:
    print("Successful")
else:
    print("notSuccessful")
