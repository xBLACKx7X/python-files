import random



while True:
	i=input("enter 'q' to quit,enter 'r' to roll")
	if(i=='q'):
		print("bye!")
		exit()

	else:
	    print("you got",random.randint(1,6))	