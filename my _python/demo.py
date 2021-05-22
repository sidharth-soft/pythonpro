# srinu = []
# for i in range(10):
#     # print(i,end=" ")
#     srinu.append(i)
# print(srinu)
# print(srinu[::-1])


'''list = [10, 20, 50, 80, 99]


abhi = set(list)
print(abhi)

abhi.remove(max(abhi))
print(abhi)

print(max(abhi))'''

neg = [-1,5,4,8,6,-2,-8,-7,1]


# for i in neg:
#
#     # if i > 0:
#     #
#     #     print(i, end=" ")
#     if i < 0:
#         print(i,end=" ")
#     else:
#         print("abhi om ")

srinu = list(filter(lambda x:x<0 ,neg))

print(srinu)


