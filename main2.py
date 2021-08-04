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

