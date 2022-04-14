def make_adder(x):
   def adder(n):
       return x + n
   return adder

add_5 = make_adder(5)
print(type(add_5))
print(add_5(10))
print(add_5(100))