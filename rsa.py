from Crypto.Util.number import  long_to_bytes, bytes_to_long
from gmpy2 import  invert


c1 = 4234670293038317987938055135294674120134854898297625935607903778512463951674936671375415169360934197229255161974541023661821569586235634402424602192238648409013774969572165200359977997303830173011967915874024945414212947446117240175983865322060043620071722279090850198558648063178334381851809435828760353131601643984698313811382380004022329209484525444198946778173170580260108395171921816477973892741883396043509219035092982222280469228397250864654187057876133668476515430916596120437196081039258573121921640329422486314571419238016553633525654867006406955213774556429006429269462557939390106901664693602730624268753
c2 = 1751865483793474627015895076955913383584042962032457228641940417031113274779177542341100780584308735055544921823105985061213807361924733124858298105604898080606350448978518476354105143921485817056604843837243559100101026529294509558374689999482515365499609888887426837474675735812277541464390585481093469666773439257938070085034128299858187130402665003220343662040930674011411472097078472386811721867965618257957575601839566711633807028861591622456575701620801673
e =  65537
n1 = 27935313681460792379089445557200781484373736631343831623603002162140882156549225786978005135341310574296130053932518796958851807095170536807862715623063938198713283366579496544087788102892453350191812399495415107249518664490700137465472130951629801129356896132956097164133885320172223567717782396107605415015802669654117436830270888444182067164914205264386861390218022711964969980534003826233266395281367865446788259413968470157493653994856168718079530741541527321212023279771564339592279369736817061517495783850389629924916811719870291845484120706196255480055334174848450732482474454421933039503848905759017324329831
n2 = 2138695492794004920577049750550914108558751244974507457524710262077209057800980008271085742575533174553500148893361563068723871194417991266906589544003916582033314597188521055514985604470147195939560697073587618937906692770395008889038849845588371690842893973542479973091147690152363759562728901632049419999085581565752609751937544307106783875625101545216827483333476225604189407479217129521300698567277854496696109027323760548430116264592138624792488027029370217
z =  11461411710138901527547487764629519734142919252323699836762026676871532600264023580385933153120750259148703327756797774096208736500160686939355263726824057

p1 =  12928209705792792571278393170673755062061690024166269969759135246019466581529356800503489684627947312774432845665852918649760723786130737575038320905878163
q1 =  12928209705792792571278393170673755062061690024166269969759135246019466581529356800503489684627947312774432845665852918649760723786130737575038320905879101
p2 =  12928209705792792571278393170673755062061690024166269969759135246019466581529356800503489684627947312774432845665852918649760723786130737575038320905879407
q2 =  12928209705792792571278393170673755062061690024166269969759135246019466581529356800503489684627947312774432845665852918649760723786130737575038320905879791

#getting the random prime used in n4
q3 = q1
p3 = int(n2 // q3)
print("p3 = ", p3)

#calculating the two phis
phi1 = (p1-1)*(q1-1)*(p2-1)*(q2-1)
phi2 = (p3-1)*(q3-1)

#calculating the two decryption keys
d1 = pow (e,-1,phi1)
d2 = pow (e,-1,phi2)
print("\nd1 = ", d1)
print("\nd2 = ", d2)

#decrypting the first part of the message c1
#first we remove the affect of integer z, which is added after encryption to add padding and randomness to the encryption for better security
z_inv = invert(z,n1)
c11 = (c1 * z_inv) % n1
#Now we can decrypt the message
pt1 = pow(c11,d1,n1)
print("\npt1 = ", pt1)
m1_bytes = long_to_bytes(pt1)
print("\nm1_bytes = ", m1_bytes)


m1 = bytes_to_long(b'EGCERT{16500bc003f74b4ba6ef96')

#initializing the variable
m2_bytes = b'EGCERT'

#we don't know the value the random int that was used to add padding and randomness after the encryption, however we know it's range
#so we can bruteforce it by iterating over all the values and check if the message is decrypted in the right way
for i in range(999,30001):
    #first we remove the effect of randomness
    padding_rand = m1 * i
    padding_inv = invert(padding_rand, n2)
    #then we decrypt the message
    c22 = (c2 * padding_inv) % n2
    pt2 = pow(c22,d2,n2)
    m2_bytes = long_to_bytes(pt2)
    #we can check if the message is decrypted and resulted in the flag, since we know the length of half the flag already and it can't exceed that number
    # It's length is expected to be 30, so the condition 30 < 50 is valid.
    # Note if the result is not the desired answer, it's in hexadecimal string and it's length is 80 or more    
    if(len(m2_bytes) < 50):
        print(m2_bytes)
        break
    else:
        print(f"using i = {i} .... \n")

print(f"\n\nThe flag is  {m1_bytes+m2_bytes}\n")