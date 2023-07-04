# EGCERT-CTFs2023-Easy_Encryption_Challenge_Writeup

Here we can notice that the used encryption is RSA, but the modulus n3 uses 4 prime numbers instead of two. However the trick is using "next_prime" in the given sequence means that the 4 primes are all successive.

n1 --> n3 = n1 * n2   
n1 = p1*q1   
n2 = p2*q2   
n1 * n2 = (p1*q1) * (p2*q2)    
p1 --> random prime with 512 bit size   
q1 --> next prime after p1   
p2 --> next prime after q1   
q2 --> next prime after p2   

![image](https://github.com/MohamedAwad9k8/EGCERT-CTFs2023-Easy_Encryption_Challenge_Writeup/assets/75997594/c98fd60e-06f1-4f03-8b9d-4ab70682c893)

And we have the output given with the source code of the encryption.

![image](https://github.com/MohamedAwad9k8/EGCERT-CTFs2023-Easy_Encryption_Challenge_Writeup/assets/75997594/799bf114-d298-41c3-bfd2-25d0915ad894)

note that n1 is n3 in the code, and n2 is n4 in the code.

Knowing that the 4 primes are successive we can work on factorizing them. 
First I tried Alberton and Factor.db but modulus (n1 from the output file) was too big.

So I worked on bruteforcing the factorization with an iterative method approach, meaning that I take the output of each iteration and use it as in input for the next iteration while decreasing the searching steps to increase the accuracy of searching. This way I decrease the complexity of bruteforcing the factorization and get a quicker result instead of waiting many hours using a simple for loop and incrementing the same small steps everytime.

Note: p1 = getPrime(512) --> means the smallest prime is a random prime with 512 bits size, so the primes are in the range of     
[2pow(1) - 2pow(15)-1] this gives us around 10pow(154) possible primes which is why normal iteration would be too slow.
