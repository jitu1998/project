class customer(object):
	def __init__(self,name):
		self.name = name
    
def set_balance(self,balance=0):
    self.balance =balance

    def withdraw(self,amount):
    	if amount>self.balance:
    		raise RuntimeError('Amount greater than available balance')
    		self.balance -= amount
    		return self.balance

    def deposit(self,amount):
    	self.balance += amount
    	return self.balance

v1=customer('priya')
v1.set_balance(40000)
print(v1.withdraw(3000))
print(v1.deposit(1000))   