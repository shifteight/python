class User():

	def __init__(self, f_name, l_name, age):
		self.first_name = f_name
		self.last_name = l_name
		self.age = age
		self.login_attempts = 0
	
	def describe_user(self):
		user_info = self.first_name + ' ' + self.last_name + ', ' + str(self.age)
		print(user_info.title())
	
	def greet_user(self):
		print("Hello, " + self.first_name + "!")
	
	def increment_login_attempts(self):
		self.login_attempts += 1
	
	def reset_login_attempts(self):
		self.login_attempts = 0


user = User("Kevin", "qian", 40)
user.describe_user()
user.greet_user()
for i in range(5):
	user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)