plaintext = input("Enter any text: ").replace(' ', '').lower()
ciphertext =""
key = int(input("Enter key value: "))
enc=[[" " for i in range(len(plaintext))] for j in range(key)]
flag=0
row=0
for i in range(len(plaintext)):
  enc[row][i]=plaintext[i]
  if row==0:
    flag=0
  elif row==key-1:
    flag=1
  if flag==0:
    row+=1
  else:
    row-=1
for i in range(key):
  print("".join(enc[i]))
ct=[]
for i in range(key):
    for j in range(len(plaintext)):
        if enc[i][j]!=' ':
            ct.append(enc[i][j])
ciphertext="".join(ct).upper()
print("Plain Text: ",plaintext)
print("Cipher Text: ",ciphertext)
    