import collections

###########点数を計算する関数############
def score(L):
    c = collections.Counter(L)
    sum=c['a']+c['b']+c['d']+c['e']+c['g']+c['i']+c['n']+c['o']+c['r']+c['s']+c['t']+c['u']
    sum+=2*(c['c']+c['f']+c['h']+c['l']+c['m']+c['p']+c['v']+c['w']+c['y'])
    sum+=3*(c['j']+c['k']+c['q']+c['x']+c['z'])
    return (sum+1)*(sum+1)
    

L2=[] #文字ソート後の辞書
newL2=[] #新しい辞書をソート
L3=[]
newL3=[]
s=''
s1=''
s2=''

#################辞書を読み込みLに代入##################
L=[] #元の辞書
dic_data = open("dictionary.words.txt","r")
lines = dic_data.readlines()
i = 0
j = 0
for line in lines:
   L.append(line)
   

#################並べ替えた辞書を作成する#################   
while i < len(L):
   s1=L[i]
   s2=s1.lower()
   char=list(s2)
   s2=''
   char.sort()
   while j < len(char):
       s += char[j]
       j += 1
   L3.append(s)    
   s=s+','+s1    
   L2.append(s)
   s1=''
   s=''
   char=[]
   i+=1
   j=0
   
newL2=sorted(L2)#元の単語を保持している辞書
newL3=sorted(L3)#比較用の辞書


####################検索文字列を入力する#####################
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
#もっといい入力方法が知りたいです

i=0
j=0
ans=''
s=0

while j<len(newL2):
    dic=list(newL3[j])
    dic.remove("\n")
    newEnt2=newEnt.copy()
    while True:      
       if(i==(len(dic))):
            if(s<score(dic)):#点数を計算して前の記録より高かったら暫定のanswerとする
                s=score(dic)
                ans=newL2[j]
            break;            
       if(dic[i] not in newEnt2):
            break; 
       else:
            newEnt2.remove(dic[i]);#一致したら入力文字列からその文字を削除
            i+=1;
    j+=1;
    i=0;
    dic=[]
    
    
print("Final answer is",ans)
dic_data.close()