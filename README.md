# HW2_hash_practice
s = open("hw2_data.txt", "r")
str = s.read()
str2 = str.split(" ")
dict1 = {}
for word in str2:
  if word in dict1:
    dict1[word] += 1
  else:
    dict1[word] = 1
print(dict1)
