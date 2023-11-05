def gcd(a, h):
	temp = 0
	while(1):
		temp = a % h
		if (temp == 0):
			return h
		a = h
		h = temp
def isprime(num1):
    b=0
    if num1==2:
        return 1
    for i in range(2,num1):
        if num1 % i==0:
            b=0
            break
        else:
            b=1
    if b==0:
        return 0
    elif b==1:
        return 1
def intcheck(e,phi):
    k=1
    while True:
        d=(1+(k*phi))/e
        if d==int(d):
            return int(d)
        else:
            k+=1
p=int(input("Enter the prime number p"))
q=int(input("Enter the prime number q"))
if isprime(p) and isprime(q):
    n=p*q
    phi=(p-1)*(q-1)
    e=2
    while e<phi:
        if gcd(e,phi)==1:
            break
        else:
            e+=1
    d=intcheck(e,phi)
    plaintext=int(input("Enter the plaintext: "))
    ciphertext=((plaintext)**e)%n
    plain=((ciphertext)**d)%n
    print(f"The Ciphertext is {ciphertext}")
    print(f"The decrypted text is {plain}")
    


        


        