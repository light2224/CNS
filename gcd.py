# def gcd(num1,num2):
#     i=1
#     g=1
#     while i <= num1 and i<= num2:
#         if num1%i==0 and num2%i==0:
#             g=i
#             i+=1
#     return g
# print(gcd(5,7))
a="aadi"
k=2
enc=[[" " for i in range(len(a))] for j in range(k)]
print(enc)
# print(enc[0])
for i in range(k):
  print("1".join(enc[i]))