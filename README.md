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

First I will run "initial_guessing_the_primes.py" so that I get a good initial guess for the prime p1, such that the product of 4 successive primes is greater than the modulus n.


![image](https://github.com/MohamedAwad9k8/EGCERT-CTFs2023-Easy_Encryption_Challenge_Writeup/assets/75997594/2253df9f-124f-4412-8aaf-99a3489a64da)

so now we have the initial guess for prime1. I will go to "descending_primes.py" and initilize prime4 with this value of prime1 we got from the terminal.
![image](https://github.com/MohamedAwad9k8/EGCERT-CTFs2023-Easy_Encryption_Challenge_Writeup/assets/75997594/57a9afb4-5701-4953-b8e4-f18ecf71704c)

now what this script does is it iterates over the primes in a descending order. since we are on the greater side of the target prime.

After running the script for few minutes it returns the primes whose product is less than n, and are very close to the answer we seek
![image](https://github.com/MohamedAwad9k8/EGCERT-CTFs2023-Easy_Encryption_Challenge_Writeup/assets/75997594/0151bc0b-23fc-45d8-abf8-33f6bed3270a)

