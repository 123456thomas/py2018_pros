class NumGet:
	def GetPrime(Num):
		"""求一个数内的所有素数"""
		list1=[2]
		for i in range(3,Num+1):
			p=len(list1)
			for j in range(0,p):
				if i%list1[j]==0:
					break
				if j==(p-1):
					list1.append(i)
		return list1

	def IsPrime(n):
		"""判断一个正整数是不是素数"""
		if n <= 1:
			return False
		for i in range(2, int(n**0.5) + 1):
			if n % i == 0:
				return False
		return True

	def commonDivisor1(num1, num2):
		"""求两个数的最大公约数"""
		if num1 < num2:
			temp = num1
			num1 = num2
			num2 = temp
		if num1 % num2 == 0:
			return num2
		else:
			num2 = num1 % num2
			return commonDivisor1(num1, num2)
