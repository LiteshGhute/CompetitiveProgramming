#Find Majority element
#Element is a majority element if it is occurring n/2 times.

def majorityElement(arr):
    count, contender = 0, 0

    #finding the contender
    for el in arr:
        if count == 0:
            contender = el
            count += 1
        elif el == contender:
            count += 1
        elif el != contender:
            count -= 1

    #checking if the given contender is a majority element or not
    count=0
    for el in arr:
        if el == contender:
            count+=1
    if count >= (len(arr)//2)+1:
        return contender
    return -1


if __name__ == '__main__':
    #taking array input
    arr = list(map(int, input().split()))

    result = majorityElement(arr)

    #printing output
    print(result)

#Time Complexity: O(n)
#Space Complexity: O(1)