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


class Privileges():

	def __init__(self):
		self.privileges = ["can add post", "can delete post", "can ban user"]
		
	def show_privileges(self):
		for p in self.privileges:
			print(p)


class Admin(User):

	def __init__(self, f_name, l_name, age):
		super().__init__(f_name, l_name, age)
		self.privileges = Privileges()


# user = User("Kevin", "qian", 40)
# user.describe_user()
# user.greet_user()
# for i in range(5):
# 	user.increment_login_attempts()
# print(user.login_attempts)
# user.reset_login_attempts()
# print(user.login_attempts)

admin = Admin("Kevin", "Qian", 40)
admin.privileges.show_privileges()