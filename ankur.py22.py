Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
def countFreq(pat, txt):
    M = len(pat)
    N = len(txt)
    res = 0
    for i in range(N - M + 1):
        j = 0
        while j < M:
            if (txt[i + j] != pat[j]):
                break
            j += 1
 
        if (j == M):
            res += 1
            j = 0
    return res
if __name__ == '__main__':
    txt = "dhimanman"
    pat = "man"
    print(countFreq(pat, txt))