class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        table = {
            "2": "abc", "5": "jkl",
            "3": "def", "6": "mno",
            "4": "ghi", "7": "pqrs",
            "8": "tuv", "9": "wxyz",
        }
        combs = []
        l = len(digits)
        def solve(combo: list[int], ind: int):
            if len(combo) == l:
                combs.append("".join(combo))
                return
            button = digits[ind]
            letters = table[button]
            for i in range(len(letters)):
                combo.append(letters[i])
                solve(combo, ind + 1)
                combo.pop()
            
        solve([], 0)
        return combs
