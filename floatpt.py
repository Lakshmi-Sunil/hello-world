def check(num):
	#print(length)
	length=len(num)
	if (num[0]=="+" or num[0]=="-"):
		index=num.find(".")
		#print(index)
		if (index==-1):
			print(False)
		elif(index==1):
			if(num[2:length].isnumeric()):
				print(True)
			else:
				print(False)
		else:
			#print(num[1:index])
			if(num[1:index].isnumeric()):
				if(num[index+1:length].isnumeric()):
					print(True)
				else:
					print(False)
			else:
				print(False)
	elif (num[0]=="."):
		if (num[1:length].isnumeric()):
			print(True)
		else:
			print(False)
	elif(num[0].isnumeric()):
		index=num.find(".")
		if (index==-1):
			print(False)
		else:
			if(num[0:index].isnumeric()):
				if(num[index+1:length].isnumeric()):
					print(True)
				else:
					print(False)
			else:
				print(False)
	else:
		print(False)
		
n=int(input())
for j in range(0,n):
	num=input()
	check(num)

	
