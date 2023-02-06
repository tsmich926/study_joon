# for t_c in range(20):
#     num = int(input())
#     jegop = num ** 2
#     jegop = str(jegop)
#     num = str(num)
#     if len(num) == 1:
#         if jegop[-1] == num:
#             print('Yes')
#         else:
#             print('No')
#     elif len(num) == 2:
#         if jegop[-1] == num[-1] and jegop[-2] == num[-2]:
#             print('Yes')
#         else:
#             print('No')
#     elif len(num) == 3:
#         if jegop[-1] == num[-1] and jegop[-2] == num[-2] and jegop[-3] == num[-3]:
#             print('Yes')
#         else:
#             print('No')
#     else :
#         if jegop[-1] == num[-1] and jegop[-2] == num[-2] and jegop[-3] == num[-3] and jegop[-4] == num[-4]:
#             print('Yes')
#         else:
#             print('No')

# T = int(input())
# for t_c in range(T):
#     num = int(input())
#     jegop = num ** 2
#     jegop = str(jegop)
#     num = str(num)

# T = int(input())
# for t_c in range(T):
#     num = int(input())
#     jegop = num ** 2
#     jegop = str(jegop)
#     num = str(num)
# if len(num) == 1:
#     if jegop[-1] == num:
#         print('Yes')
#     else:
#         print('No')
# elif len(num) == 2:
#     if jegop[-1] == num[-1] and jegop[-2] == num[-2]:
#         print('Yes')
#     else:
#         print('No')
# elif len(num) == 3:
#     if jegop[-1] == num[-1] and jegop[-2] == num[-2] and jegop[-3] == num[-3]:
#         print('Yes')
#     else:
#         print('No')
# else :
#     if jegop[-1] == num[-1] and jegop[-2] == num[-2] and jegop[-3] == num[-3] and jegop[-4] == num[-4]:
#         print('Yes')
#     else:
#         print('No')


# T = int(input())
# lst = []
# for t_c in range(T):
#     num = int(input())
#     jegop = num ** 2
#     jegop = str(jegop)
#     num = str(num)
#     if len(num) == 1:
#         if jegop[-1] == num:
#             lst.append('Yes')
#         else:
#             lst.append('No')
#     elif len(num) == 2:
#         if jegop[-1] == num[-1] and jegop[-2] == num[-2]:
#             lst.append('Yes')
#         else:
#             lst.append('No')
#     elif len(num) == 3:
#         if jegop[-1] == num[-1] and jegop[-2] == num[-2] and jegop[-3] == num[-3]:
#             lst.append('Yes')
#         else:
#             lst.append('No')
#     else :
#         if jegop[-1] == num[-1] and jegop[-2] == num[-2] and jegop[-3] == num[-3] and jegop[-4] == num[-4]:
#             lst.append('Yes')
#         else:
#             lst.append('No')
# for i in lst:
#     print(i)

T = int(input())
lst = []
for tc in range(T):
    N = int(input())
    square = str(N*N)
    N_len = len(str(N))
    if square[-N_len:] == str(N):
        lst.append("Yes")
    else:
        lst.append("No")
for i in lst:
    print(i)