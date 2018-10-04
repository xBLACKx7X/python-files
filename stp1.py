
import random
a={1:'r',2:'p',3:'s'}
b=input("enter rock,paper or scissor")
c=a[random.randint(1,3)]
print(c)
if(c==b):
	print("its a tie")
elif((c=='r' and b=='p') or (c=='p' and b=='s') or (c=='s' and b=='r')):
	print("you win")
else:
	print(" computer wins")		
