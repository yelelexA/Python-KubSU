#task 1
# f = open('input1.txt','r')
# text = f.read()
# words= text.split()
# print(len(words))
# f.close()

#task 2
# f = open('input2.txt')
# text = f.readlines()
# for i in text:
#     numbers = []
#     numbers = list(map(int,i.split()))
#     print(sum(numbers))
# f.close()

#task 3
# f = open('input5.txt')
# text = f.read()
# l = list()
#
# for i in text:
#     if i.isalpha() != True:
#         text = text.replace(i," ")
#
# words = text.split()
#
# for i in words:
#     a = (words.count(i),i)
#     if a not in l:
#      l.append(a)

# print(sorted(l))
#
# # l.sort(key = lambda x: (x[0], x[1]))
# # print(l)
#
# f.close()

#task 4
# f = open('input4.txt')
# text = f.readlines()
#
# for i in text[::-1]:
#     print(i)
#
# f.close()

#task 5
# f = open('input5.txt')
# text = f.read()
# str = text.split('\n')
# sum_letters = 0
# sum_words = 0
#
# print(len(text.split('\n')))  #strok
# for i in text:
#    if i.isalpha():
#        sum_letters+=1
#    else:
#       text=text.replace(i," ")
# #
# # words =text.split()
# # for i in words:
# #     if i.isalpha():
# #         sum_words += 1
#
#
# print(sum_letters)
#
# # print(sum_words)
# print(len(text.split())) #slov
#
# f.close()

#task 6
# f = open('input6.txt')
# text = f.read()
# print(text[::-1])
# f.close()


#Individualka
f = open('indiv.txt')
text = f.read()
l = list()
print(text)
start=0
for i in range(len(text)):
    if text[i] == ")":
        d = 1
        start = i
        while d != 0:
            start -= 1
            if text[start] == "(":
                d -= 1
            if text[start] ==")":
                d += 1

        l.append((start,i))
print(l)
print(sorted(l))
