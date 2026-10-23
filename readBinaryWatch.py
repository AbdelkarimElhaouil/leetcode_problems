class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        res = []
        minutes = [0, 1, 2, 4, 8, 16, 32]
        hours = [0, 1, 2, 4, 8]
        def solve(h_used: list[int], m_used: list[int], h_sum: int, m_sum: int):
            if len(h_used) + len(m_used) == turnedOn:
                return

            for i in range(hours):
                if h_sum + hours[i] > 11:
                    return
                h_used.append(hours[i])
                solve(h_used, m_used, h_sum + hours[i], m_sum)
                for i in range(len(minutes)):
                    if len(h_used) + i + 1 > turnedOn:
                        break
                    elif minutes[i] + m_sum > 59:
                        
                
                h_used.pop()

