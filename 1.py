m = {} # { num : index }
nums = [11, 2, 15, 7]
target = 9

for i in range(len(nums)):
    num = nums[i]
    diff = target - num
    if diff in m:
        print(True)
    else:
        m[num] = i

    print(m)