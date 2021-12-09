#1.1
#for i in range(100,1000):
#   if i*i%1000 == i:
#    print(i)

#1.2

#n = int(input())

#for i in range(100,1000):
#    if i%10+i//10%10+i//100 == n:
#        print(i)

#1.3

#A=int(input())
#B=int(input())

#for i in range(A,B+1):
#    str_i=str(i)
#    if str_i == str_i[::-1]:
#        print(i)

#1.4
#A = int(input())
#B = int(input())

#for i in range(A, B+1):
#    str_i = str(i)
#    for j in range(1, 4):
#      if str_i.count(str_i[j]) == 3:
#        print(i)

#2.1

# a = input().split()
#
# max = cur_max = 1
#
# for i in range(0,len(a)):
#     if a[i] != a[i-1]:
#         cur_max = 1
#     else:
#         cur_max += 1
#
#     if max < cur_max:
#         max = cur_max
#
# print(max)

#2.2
# a = input().split()
#
# m1 = 0
# m2 = 0
#
# count = 0
# for i in range(len(a)-1):
#     if a[i] > a[i+1]:
#         count += 1
#     else:
#         m1 = max(m1, count)
#         count = 0
#
# m1 = max(m1, count)
# count = 0
# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         count += 1
#     else:
#         m2 = max(m1, count)
#         count = 0
# m2 = max(m1, count)
#
# print(max(m1, m2))

#2.3
# a = input().split()
# count = 0
#
# for i in range(len(a)-1):
#     if a[i] > a[i-1]:
#         if a[i] > a[i+1]:
#          count += 1
#
# print(count)

#2.4
# a = input().split()
# x = list()
#
# for i in range(len(a)-1):
#     if a[i] > a[i-1]:
#         if a[i] > a[i+1]:
#          x.append(i)
#
# m=len(a)
# for i in range(len(x)):
#     if abs(x[i]-x[i-1]) < m:
#         m = abs(x[i] - x[i-1])
#
# print(m-1)

#3.1
# ch1={'yellow','red','blue','black'}
# ch2={'black','white','yellow'}
#
# print("Пересечение",ch1.intersection(ch2))
# print("Объединение",ch1.union(ch2))
# print("Цвета, которые есть только у первого",ch1.difference(ch2), " и у второго ",ch2.difference(ch1))

#3.2
#есть кол-во детей, для каждого ребенка есть кол-во языков, которые он знает и сами языки.
#Найти кол-во и сами языки, которые знают все дети и языки, которые знает хотя бы один.

# print("Введите кол-во детей")
# n=int(input())
# print("Введите языки для 1-го ребенка")
# ch=set(map(str,input().split()))
#
# ch_intersection=ch
# ch_union=ch
#
# for i in range(n-1):
#     print("Введите языки для",i+2,"-го ребенка")
#     x=set(map(str,input().split()))
#     ch_union=ch_union.union(x)
#     ch_intersection=ch_intersection.intersection(x)
#
# print("Пересечение",ch_intersection,"Объединение",ch_union)

#3.3
# Дано кол-во дней, кол-во политический партий. Для каждой полит. партии заданы 2 числа
#1 - первый день забастовки
#2 - период (через сколько повторяется)
#Первый день всегда понедельник (1-число) и суббота, воскресенье всегда выходной
#Сколько дней страна работала?

n_all_days = int(input("Введите количество дней:"))
n_parties = int(input("Введите количество партий партий:"))

all_days = set()
weekends = set()

for i in range(1,n_all_days+1):
    all_days.add(i)

for i in range(6,n_all_days+1,7):
    weekends.add((i))
    weekends.add((i+1))

weekends.intersection_update(all_days)
all_days.difference_update(weekends)

for i in range(n_parties):
    print("Введите первый день забастовки для ",i+1," партии :")
    first_day = int(input())
    period = int(input("Введите период :"))
    for j in range(first_day,n_all_days+1,period):
       strike_days = set()
       strike_days.add(j)
       all_days.difference_update(strike_days)

print("Страна работала в этих числах:",all_days,"Т.е. ",len(all_days),"из",n_all_days,"дней")

