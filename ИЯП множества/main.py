# #1
# n=int(input())
#
# dictionary=dict()
#
# for i in range(n):
#    key=input()
#    value=input()
#    dictionary[key]=value
#
# print(dict)
# word=input()
#
# if word in dict.keys():
#    print(dictionary[word])
#
# for keys,values in dictionary.items():
#    if values==word:
#       print(keys)

#2
# str=input().split()
# dictionary={i:0 for i in set(str)}
#
# for i in str:
#     print(dictionary[i])
#     dictionary[i]+=1
#
# print(dictionary)

#3
# str=input().split()
# dictionary={i:0 for i in set(str)}
#
# for i in str:
#     dictionary[i]+=1
#
# max=0
# max_word=list()
#
# for key,value in dictionary.items():
#     if value > max:
#         max=value
#
# for key,value in dictionary.items():
#         if value == max:
#          max_word.append(key)
#
# max_word.sort()
#
# print(max_word[0])

#4
n=int(input())
dictionary=dict()

for i in range(n):
    str=input().split()
    dictionary[str[1]]=str[0]

countries=list()
for key in dictionary.keys():
    countries.append(key)

countries.sort()

for i in countries:
    print(dictionary[i],i)

#5







