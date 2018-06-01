L=[] #元の辞書
L2=[] #文字ソート後の辞書
newL2=[] #新しい辞書をソート
L3=[]
newL3=[]
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
   L3.append(s)
   s=''
   char=[]
   i+=1
   j=0
   
newL3=sorted(L3)


i=0
j=0
   

while i < len(L):
   s1=L[i]
   s2=s1.lower()
   char=list(s2)
   s2=''
   char.sort()
   while j < len(char):
       s += char[j]
       j += 1
   s=s+','+s1    
   L2.append(s)
   s1=''
   s=''
   char=[]
   i+=1
   j=0
   
newL2=sorted(L2)


Ent=[]#入力文字列
E=''

#０が入力されるまで入力を続ける
while True: 
  x=input("Input word:")
  if(x== '0'):
      break;
  Ent.append(x);
    
        
print(Ent) 
newEnt=sorted(Ent) 
print(newEnt) 

i=1
j=0

dic=list(newL3[j])
print(dic)

while j<len(newL2):
    dic=list(newL3[j])
    while True:
        if(dic[i] not in newEnt[i-1:]):
            break;          
        if(i==(len(dic)-1)): 
            print(newL2[j])
            break;         
        i+=1
        
    j+=1;
    i=1;
    dic=[]
    
dic_data.close()