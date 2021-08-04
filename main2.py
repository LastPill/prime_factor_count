def list_of_prime(n):
    list_n = [2]
    for num in range(3, abs(min(n)), 2):
        prime = True
        for i in range(2,num):
            if (num%i==0):
                prime = False
        if prime:
            list_n.append(num)
    return list_n

def sum_for_list(lst):
    ans = []
    all_list = []
    for i in list_of_prime(lst):
        list = [x%i for x in lst]
        if 0 in list:
            k = 0
            while 0 in list:
                ans.append(lst[list.index(0) + k])
                list.pop(0)
                k += 1
    return ans





    #         list = []
    #         for k in lst:
    #             if k%i == 0:
    #                 list.append(k)
    #         if len(list) != 0:
    #             all_list.append([i, sum(list)])
    # return all_list

print(sum_for_list([200000, 2100880, 2408800, 3088000, 4500880]))

# def natural(k):
#     if k % 2 == 0:
#         return k == 2
#     d = 3
#     while d * d <= k and k % d != 0:
#         d += 2
#     return d * d > k

# def natural_list(p):
#     list_n = [2]
#     for i in range(3, abs(min(p)), 2):
#         if natural(i) == True:
#             list_n.append(i)
#     return list_n


