def lcs(s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0
    if s1[i] == s2[j]:
        return 1 + lcs(s1, s2, i + 1, j + 1)
    else:
        return max(lcs(s1, s2, i + 1, j), lcs(s1, s2, i, j + 1))

def lcs_back(s1, s2, i, j, memo):
    if i == len(s1) or j == len(s2):
        return ""

    if (i, j) in memo:
        length = memo[(i, j)]
    else:
        if s1[i] == s2[j]:
            length = 1 + lcs(s1, s2, i + 1, j + 1)
        else:
            length = max(lcs(s1, s2, i + 1, j), lcs(s1, s2, i, j + 1))
        memo[(i, j)] = length

    if s1[i] == s2[j]:
        return s1[i] + lcs_back(s1, s2, i + 1, j + 1, memo)
    else:
        len1 = lcs(s1, s2, i + 1, j)
        len2 = lcs(s1, s2, i, j + 1)
        if len1 > len2:
            return lcs_back(s1, s2, i + 1, j, memo)
        else:
            return lcs_back(s1, s2, i, j + 1, memo)

if __name__ == "__main__":
    str1 = "BDCABA"
    str2 = "ABCBDAB"
    length = lcs(str1, str2, 0, 0)
    memo = {}
    lcs1 = lcs_back(str1, str2, 0, 0, memo)
    print(f"Length of LCS: {length}")
    print(f"Longest Common Subsequence: {lcs1}")