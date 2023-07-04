import sympy

n = 27935313681460792379089445557200781484373736631343831623603002162140882156549225786978005135341310574296130053932518796958851807095170536807862715623063938198713283366579496544087788102892453350191812399495415107249518664490700137465472130951629801129356896132956097164133885320172223567717782396107605415015802669654117436830270888444182067164914205264386861390218022711964969980534003826233266395281367865446788259413968470157493653994856168718079530741541527321212023279771564339592279369736817061517495783850389629924916811719870291845484120706196255480055334174848450732482474454421933039503848905759017324329831
#Intitilizing values for the four primes
prime4 = 12929898555215726034563221387459383840897352767578942692610709223290103982832775194477046741164594724722459549666915569561791036493874367044415902502076513
prime3 = sympy.prevprime(prime4)
prime2 = sympy.prevprime(prime3)
prime1 = sympy.prevprime(prime2)
#Diff_value is a value I use to increase step size while iterating to reach the limit faster (product < n)
#The Diff_value then gets smaller to increase accuracy as I approach the target prime
# diff_value has a range from 150 digits to 3 digits then, I stop iterating.
const_99 = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
diff_value = const_99


iteration = 0
while (iteration < 50):
    diff_value = const_99 // pow(10,(3 * iteration))    
    print("\n\n______________________________________________")
    print(f"\n\nStarting New Iteration, Iteration #{iteration}")
    print("\n\n______________________________________________")
    print(f"diff value = {diff_value}")
    trial = 0
    while trial < 2000:

        print(f"\n\nTrial : {trial} in Iteration : {iteration}\n\n")
        prime3 = sympy.prevprime(prime4)
        prime2 = sympy.prevprime(prime3)
        prime1 = sympy.prevprime(prime2)
        product = prime1 * prime2 * prime3 * prime4
        print("Prime1 : ", prime1, "\n\n")
        print("Prime2 : ", prime2, "\n\n")
        print("Prime3 : ", prime3, "\n\n")
        print("Prime4 : ", prime4, "\n\n")
        print("product : ", product, "\n\n")
        if product > n:
            print("The product of 4 successive prime numbers is greater than n")
            prime4 = sympy.prevprime(prime1 - diff_value)
            #updating the value with the last value that satisifies the condition
            prime1_old = prime1 
        elif product == n:
            print("The product of 4 successive prime numbers is equal than n ====")
            break
        else:
            print("The product of 4 successive prime numbers is less than n")
            break
        trial += 1
    #starting a new iteration with the output of the last as it's input
    # this way the new input has less error percentage and so we can use smaller steps for higher accuracy
    # We make sure to update the value using the last valid value from the trial just before the trial that led to product less than n   
    prime4 = prime1_old
    iteration +=1

