import math

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows:
            return s
        result = ""
        table = [[] for _ in range(numRows)]
        index = 0
        while index < len(s):
            for i, row in enumerate(table):
                if index + i >= len(s):
                    break
                row.append(s[index + i])
            index += numRows
            for i in range(1, numRows - 1):
                row = table[numRows - i - 1]
                if index >= len(s):
                    break
                row.append(s[index + i - 1])
            index += numRows - 2
        for row in table:
            result += ''.join(row)
        
        return result