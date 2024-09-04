# def add(a,b):
#     return a+b

# class Test:
#     def __init__(self,add_function):
#         self.add_function = add_function


# test = Test(add_function = add)
# print(test.add_function(1,2))

class Monster:
    def __init__(self,func):
        self.func = func

class Attacks:
    def bite(self):
        print('bite')

    def strike(self):
        print('strike')

    def slash(self):
        print('slash')

    def kick(self):
        print('kick')
attacks = Attacks()
monster = Monster(func = Attacks().bite)
monster.func()