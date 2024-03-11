class Solution:
    def reverseSingleWord(self, s: str, start: int, end: int) -> str:
        word = s[start:end+1]
        left, right = 0, len(word) -1
        result = ['']*(right+1)
        
        while left <= right:
            result[left], result[right] = word[right], word[left]
            left, right = left + 1, right - 1
        
        return "".join(result)

    def reverseWords(self, s: str) -> str:
        start = end = 0
        results = []
        n = len(s)
        for i in range(n):
            if s[i] == ' ' or i==n-1:
                end = n if i == n - 1 else i - 1
                word = self.reverseSingleWord(s,start,end)
                results.append(word)
                start = i + 1
        return " ".join(results)

# java
"""
Using 1 Array chArray
Instead of creating multiple ones "result" like above

class Solution {

    public String reverseWords(String s) {
        int lastSpaceIndex = -1;
        char[] chArray = s.toCharArray();
        int len = s.length();
        for (int strIndex = 0; strIndex <= len; strIndex++) {
            if (strIndex == len || chArray[strIndex] == ' ') {
                int startIndex = lastSpaceIndex + 1;
                int endIndex = strIndex - 1;
                while (startIndex < endIndex) {
                    char temp = chArray[startIndex];
                    chArray[startIndex] = chArray[endIndex];
                    chArray[endIndex] = temp;
                    startIndex++;
                    endIndex--;
                }
                lastSpaceIndex = strIndex;
            }
        }
        return new String(chArray);
    }

}
"""
