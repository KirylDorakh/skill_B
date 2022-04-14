age = 25

my_age = "I'm " + str(age)
print(my_age)

wow = 'wow'
print(wow*5)

age1 = 26
my_age1 = "I'm %d years old"%(age1)
print(my_age1)

pi = 31.4159265
print ("%.4e" % (pi))

day = 14
month = 2
year = 2012

print("%d.%02d.%d" % (day, month, year))
# 14.02.2012
print("%d-%02d-%d" % (year, month, day))
# 2012-02-14
print("%d/%d/%d" % (year, day, month))
# 2012/14/2
print("%02d:%012d:%02d" % (day, month, year))