# (вес, рост)
data = [
   (82, 1.91),
   (68, 1.74),
   (90, 1.89),
   (73, 1.79),
   (76, 1.84)
]


result = sorted(list(map(lambda weight_height: weight_height[0]/(weight_height[1])**2, data)))
print(result)
# or
print(sorted(data, key=lambda x: x[0] / x[1] ** 2))
print(min(data, key=lambda x: x[0] / x[1] ** 2))
