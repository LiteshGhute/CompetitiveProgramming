#Find Majority element
#Element is a majority element if it is occurring n//3 times.

def majorityElement(arr):
    count1, count2, contender1, contender2 = 0, 0, -1, -1

    #finding the contender
    for el in arr:
        if count1 == 0:
            contender1 = el
            count1 += 1
        elif count2 == 0 and contender1 != el:
            contender2 = el
            count2 += 1
        elif el == contender1:
            count1 += 1
        elif el == contender2:
            count2 += 1
        elif el != contender1 and el != contender2:
            count1 -= 1
            count2 -= 1

    #checking if the given contender is a majority element or not
    count1, count2 = 0, 0
    for el in arr:
        if el == contender1:
            count1 += 1
        if el == contender2:
            count2 += 1
    res = []
    if count1 >= (len(arr)//3)+1:
        res.append(contender1)
    if count2 >= (len(arr)//3)+1:
        res.append(contender2)
    return res


if __name__ == '__main__':
    #taking array input
    arr = list(map(int, input().split()))

    result = majorityElement(arr)

    #printing output
    if len(result) == 0:
        print(-1)
    else:
        print(*result)

#Time Complexity: O(n)
#Space Complexity: O(1)