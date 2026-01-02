class Solution:
    def convert(self, s: str, numRows: int) -> str:
        index = 0
        s_len = len(s)
        result = [[] for _ in range(numRows)]
        while index < s_len:
            for i in range(numRows):
                if index >= s_len:
                    break
                result[i].append(s[index])
                index += 1
            if index < s_len:
                for i in range(numRows - 2):
                    if index >= s_len:
                        break
                    j = numRows - 2 - i
                    result[j].append(s[index])
                    index += 1
        result_s = ""
        return "".join("".join(row) for row in result)
