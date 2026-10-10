def lengthOfLongestSubstring(self, s: str) -> int:
    ans = 0
    left = 0
    m = {}

    for right in range(len(s)):
        if s[right] not in m:
            m[s[right]] = 0
        m[s[right]] += 1

        while m[s[right]] > 1:
            m[s[left]] -= 1
            left += 1
            if m[s[left]] == 0:
                del m[s[left]]

        ans = max(ans, right - left + 1)

    return ans