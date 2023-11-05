plain=input("Enter the plain text")
cipher=""
alpha="abcdefghijklmnopqrstuvwxyz"
p=plain.replace(" ","")
p1=p.lower()
k=6
for i in p1:
    temp=(alpha.index(i)+k)%26
    cipher+=alpha[temp]
print("Cipher text for the plain text ",plain," is ",cipher)
plaintext=""
for j in cipher:
    temp1=(alpha.index(j)-k)%26
    plaintext+=alpha[temp1]
print("Cipher text for the plain text ",cipher," is ",plaintext)
