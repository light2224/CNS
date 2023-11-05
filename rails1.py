plaintext=input("Enter the plaintext: ")
plaintext=plaintext.replace(" ","").lower()
ciphertext=""
key=int(input("Enter the value of a key: "))
enc=[[" "for i in range(len(plaintext))]for j in range(key)] #creating a 2D List
flag=0
row=0
for i in range(len(plaintext)): #traversing thr plaintext
    enc[row][i]=plaintext[i]
    if row==0:
        flag=0
    elif row==key-1:
        flag=1
    if flag==0:
        row+=1
    elif flag==1:
        row-=1
ct=[]
for i in range(key):        #Printing the cuiphertext
    for j in range(len(plaintext)):
        if enc[i][j]!=" ":
            ct.append(enc[i][j])
ciphertext="".join(ct)
print("Plain Text: ",plaintext)
print("Cipher Text: ",ciphertext)
    

        
