#  1. and: если все операнды являются истинными (ненулевые или непустые), то возвращается последнее истинное значение.
print('1. ', 1 and 'hello' and [False])

#  Несмотря на то, что последний операнд похож на False, он является непустым списком, а значит он истинный.

#  2. and: если один из операндов является ложным, то возвращается первый такой операнд
print(42 and 0 and '' and False)

#  3. or: если один из операндов является истинным, то возвращается первый такой операнд, а остальные игнорируются
print([] or 3.14 or False)

# 4. or: если все операнды являются ложными, то возвращается последний
print(0 or '' or False)