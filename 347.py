def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    freq = {}
    ans = []

    for num in nums:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1

    # print("FREQUENCY: ", freq)

    while k > 0:
        mostAppearedKey = None
        currMax = -1

        for key, value in freq.items():
            if freq[key] > currMax:
                currMax = value
                mostAppearedKey = key

                # print("MOST APPEARED KEY: ", mostAppearedKey)

        ans.append(mostAppearedKey)
        freq.pop(mostAppearedKey, None)

        k -= 1

        # print(ans)
    return ans