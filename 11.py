def maxArea(self, heights: List[int]) -> int:
    left = 0
    right = len(heights) - 1

    ans = 0

    while left < right:
        minHeight = min(heights[left], heights[right])
        curr = minHeight * (right - left)
        ans = max(curr, ans)

        if heights[left] < heights[right]:
            left += 1

        else: 
            right -= 1

    return ans

print(maxArea([1,8,6,2,5,4,8,3,7]))