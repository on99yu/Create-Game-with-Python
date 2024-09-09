# def relly_important_function_name():
# 	pass

# user_input = input('Presss a button')

# try:
# 	print(a)
# 	print(1/0)
# except ZeroDivisionError:
# 	print('you cannot divide by 0')
# except NameError:
# 	print('Does not exist')
# else:
# 	print('The else statement')
# finally:
# 	print('finally')

#raising exceptions
# var_must_be_string = []
# if isinstance(var_must_be_string,str):
# 	print(var_must_be_string)
# else:
# 	raise TypeError('Must be a string')

#assert
# a = 6
# assert a ==5

# my_list = [1,2,3,4,5]
# try:
# 	my_list[99]
# except IndexError:
# 	print("That index does not exist")
# else:
# 	print("That index exists")

def func():
	print("Function")

def wrapper(func):
	print('hello')
	func()
	print('goodbye')

def function_generator():
	def new_function():
		print("new fuction")
	return new_function


# wrapper(func)  	
new_func = function_generator()
new_func()	 
