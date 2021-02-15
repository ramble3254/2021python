# n = 0
# while n < 5:
#     if n == 3:
#         break
#     print(n)
#     n += 1

# print("最後的n: ", n)



# print("--------------")

# n = 0
# for x in range(4):
#     if x % 2 == 0:
#         continue
#     print(x)
#     n += 1
# print("最後的n: ", n)


n = int(input("Please enter any number: "))
for i in range(n):
    if i * i == n:
        print("整數平方根為: ", i)
        break
else:
    print("沒有整數平方根")