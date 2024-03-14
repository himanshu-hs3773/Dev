str1 = "First string"
str2 = "Second string"
matched_set = set(str1.split()) & set(str2.split())
print([s for s in str1.split() if s not in matched_set] + [s for s in str2.split() if s not in matched_set])
print(matched_set)

n = 2
my_dict = {"laptop": 999, "smartphone": 999, "smart tv": 500, "smart watch": 300, "smart home": 9999999}

print(sorted(my_dict.items(), key=lambda x: (x[1], x[0])))
print(sorted(my_dict.items(), key=lambda x: (x[1], x[0]))[n-1][0])
