L=[] #元の辞書
L2=[] #文字ソート後の辞書
newL2=[] #新しい辞書をソート
s=''
s1=''
s2=''

#辞書を読み込んで新しい辞書を作る
dic_data = open("dictionary.words.txt","r")
lines = dic_data.readlines()

i = 0
j = 0
for line in lines:
   L.append(line)
   

while i < len(L):
   s1=L[i]
   s2=s1.lower()
   char=list(s2)
   s1=''
   s2=''
   char.sort()
   while j < len(char):
       s += char[j]
       j += 1
   L2.append(s)
   s=''
   char=[]
   i+=1
   j=0
   
newL2=sorted(L2)

Ent=[]#入力文字列
E=''

i=0
while i<16:
   x=input("Input word:")
   Ent.append(x);
   i+=1
      
print(Ent) 
newEnt=sorted(Ent) 
print(newEnt) 

i=0
while i<len(Ent):
   E+=Ent[i]
   i+=1

##########二分法に改良する＃＃＃＃＃＃＃＃＃＃＃＃
i=0
while True:
   if E == newL2[i]:
       break
   i+=1
   if i == len(L2):
       print("Not found")
       break
   

j=0
while True:
   if newL2[i]==L2[j]:
       break
   j+=1
   
print(L[j])  

    
   
dic_data.close()