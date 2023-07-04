from gmpy2 import next_prime

n = 27935313681460792379089445557200781484373736631343831623603002162140882156549225786978005135341310574296130053932518796958851807095170536807862715623063938198713283366579496544087788102892453350191812399495415107249518664490700137465472130951629801129356896132956097164133885320172223567717782396107605415015802669654117436830270888444182067164914205264386861390218022711964969980534003826233266395281367865446788259413968470157493653994856168718079530741541527321212023279771564339592279369736817061517495783850389629924916811719870291845484120706196255480055334174848450732482474454421933039503848905759017324329831
prime1 = 12928209705792792571278393170673755062061690024166269969759135246019466581529356800503489684627947312774432845665852918649760723786130737575038320905877263 
prime2 = 12928209705792792571278393170673755062061690024166269969759135246019466581529356800503489684627947312774432845665852918649760723786130737575038320905877827
prime3 = 12928209705792792571278393170673755062061690024166269969759135246019466581529356800503489684627947312774432845665852918649760723786130737575038320905878163
prime4 = 12928209705792792571278393170673755062061690024166269969759135246019466581529356800503489684627947312774432845665852918649760723786130737575038320905879101

i = 0
while i < 10000:
    print(f"trial #{i}\n")
    product = prime1 * prime2 * prime3 * prime4
    if (product == n):
        print("Product of the 4 successive primes is equal to the modulus")
        print(f"\n\n p1 --> {prime1}")
        print(f"\n\n q1 --> {prime2}")
        print(f"\n\n p2 --> {prime3}")
        print(f"\n\n q2 --> {prime4}")
        break
    elif( product > n):
        print("Product of the 4 successive primes is bigger than the modulus")
        print(f"\n\n p1 --> {prime1} leads to product greater than n")
        break
    elif( product < n):
        print("Product of the 4 successive primes is smaller than the modulus")
    #incrementing the counter
    i += 1
    #updating the values of the primes with 1 step
    prime1 = prime2
    prime2 = next_prime(prime1)
    prime3 = next_prime(prime2)
    prime4 = next_prime(prime3)