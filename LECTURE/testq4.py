class SavingAccount:
	def __init__(self, bank_name, acc_name, acc_id, balance, transaction_history = []):
		self.bank_name = bank_name
		self.acc_name = acc_name
		self.acc_id = acc_id
		self.balance = balance
		self.transaction_history = transaction_history

	def deposit(self, money, person, date):
		self.balance += money
		self.transaction_history.append(["Deposit", money, self.balance, person, date])

	def withdraw(self, money, person, date):
		if self.balance < money:
			return print("Insufficient Fund")
		
		self.balance -= money
		self.transaction_history.append(["Withdraw", money, self.balance, person, date])
  
	
	def get_balance(self):
		return self.balance
	
	def print_statement(self):
		print(f"\n{'Type':-^10}|{'Amount':-^10}|{'Balance':-^10}|{'Person':-^10}|{'Date':-^10}")
		for i in self.transaction_history:
			print("{:<10}|{:<10}|{:<10}|{:<10}|{:<10}".format(i[0], i[1], i[2], i[3], i[4]))

class OverDrawnAccount(SavingAccount):
	def __init__(self, bank_name, acc_name, acc_id, balance, overdrawn_limit, transaction_history = []):
		super().__init__(bank_name, acc_name, acc_id, balance, transaction_history)
		self.overdrawn_limit = overdrawn_limit

	def withdraw(self, money, person, date):
		if self.balance - money < -self.overdrawn_limit:
			return print("XXXXXXXXXXXX Overdrawn limit reached XXXXXXXXXXXX")
	 
		self.balance -= money
		self.transaction_history.append(["Withdraw", money, self.balance, person, date])
  
overdrawn = OverDrawnAccount("Overdawn", "John", "123456", 100, 500)

overdrawn.deposit(100, "John", "2020-01-01")
overdrawn.withdraw(200, "John", "2020-01-02")
overdrawn.withdraw(502, "John", "2020-01-03")
overdrawn.print_statement()