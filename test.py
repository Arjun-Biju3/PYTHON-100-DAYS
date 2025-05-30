# def armstrong(num):
#     power = len(str(num))
#     sum = 0
#     for i in str(num):
#         sum +=  int(i)**power
#     return num == sum

# print(armstrong(9474))
# from collections import defaultdict
# anamap = defaultdict(list)
# strs = ["eat","tea","tan","ate","nat","bat"]
# for i in strs:
#     key = "".join(sorted(i))
#     anamap[key].append(i)
# print(list(anamap.values()))
s = "a good   example"
s = s.split()
# s = s[::-1]
print(" ".join(reversed(s)))