def sessionkey(g,p,private,public):
    sessionkey=(public ** private)%p
    return sessionkey
g=7
p=23
alicprivetkey=int(input("Alice private key: "))