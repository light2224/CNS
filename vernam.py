alpha="abcdefghijklmnopqrstuvwxyz"
plaintext=input("Enter the plain text")
k="password"
cipher=""
if(len(plaintext)==len(k)):
    p=plaintext.replace(" ","")
    plain=p.lower()
    for i in range(0,len(k)):
        add=alpha.index(plain[i])+alpha.index(k[i])
        if add>25:
            add-=26
            cipher+=alpha[add]
        else:
           cipher+=alpha[add] 
    print(f"The cipher text for {plaintext} is {cipher}")
else:
    print("Error")
if(len(cipher)==len(k)):
    d=""
    for i in range(0,len(k)):
        add=alpha.index(cipher[i])-alpha.index(k[i])
        if add>=25:
            add-=26
            d+=alpha[add]
        else:
          d+=alpha[add]
    print(f"The plaintext text for {cipher} is {d}")
else:
    print("Error")  
