def test_function(content):
	print(f"this is an imported function with {content}")

class Test:
	def __init__(self):
		self.name ='My App'
		self.value = 123

	def do_something(self):
		print('hello')
test_var = 'test'

def sum_calculator(*nums):
	return sum(nums)

if __name__ == '__main__':
	print(__name__)