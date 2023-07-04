from Crypto.Util.number import getPrime
from gmpy2 import next_prime
import sympy

n = 27935313681460792379089445557200781484373736631343831623603002162140882156549225786978005135341310574296130053932518796958851807095170536807862715623063938198713283366579496544087788102892453350191812399495415107249518664490700137465472130951629801129356896132956097164133885320172223567717782396107605415015802669654117436830270888444182067164914205264386861390218022711964969980534003826233266395281367865446788259413968470157493653994856168718079530741541527321212023279771564339592279369736817061517495783850389629924916811719870291845484120706196255480055334174848450732482474454421933039503848905759017324329831
prime1 = getPrime(512)
prime2 = next_prime(prime1)
prime3 = next_prime(prime2)
prime4 = next_prime(prime3)

max_p1 = sympy.prevprime(pow(2,512) - 1)

product = prime1 * prime2 * prime3 * prime4

if (product < n):
     print("Product of the 4 successive primes is smaller than the modulus\n")
     primes_diff = max_p1 - prime1
elif(product > n):
     print("Product of the 4 successive primes is greater than the modulus\n")
     print(f"Prime1 : {prime1}")
else:
     print("Product of the 4 successive primes is equal to the modulus\n")
     print(f"Prime1 : {prime1}")

i = 0
while (i < 1000):
    print(f"trial #{i}\n")
    prime1 = next_prime(prime1 + (primes_diff//100))
    prime2 = next_prime(prime1)
    prime3 = next_prime(prime2)
    prime4 = next_prime(prime3)
    product = prime1 * prime2 * prime3 * prime4

    if (product < n):
        print("Product of the 4 successive primes is smaller than the modulus\n")
        primes_diff = max_p1 - prime1 
    elif(product > n):
        print("Product of the 4 successive primes is greater than the modulus\n")
        print(f"Prime1 : {prime1}")
        break
    else:
        print("Product of the 4 successive primes is equal to the modulus\n")
        print(f"Prime1 : {prime1}")
        print(f"Prime2 : {prime2}")
        print(f"Prime3 : {prime3}")
        print(f"Prime4 : {prime4}")
        break
    i += 1
