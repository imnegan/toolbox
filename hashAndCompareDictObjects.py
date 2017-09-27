class stringy:
	
	def __init__(self, a, b, c):
		self.a=a
		self.b=b
		self.c=c
	
	def __repr__(self):
		return str(self.__dict__)
		
	def __eq__(self, other): 
		return self.__dict__ == other.__dict__
		
	def __hash__(self):
		return hash(str(self.__dict__))
		
s=stringy('a', 'b', 'c')
t=stringy('a', 'b', 'c')
print(s.a)
print(t.a)

print(s is t)

stringys=set()

stringys.add(s)
print(stringys)
stringys.add(t)
print(stringys)

print(s==t)