class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        if turnedOn > 8:
            return []
        res = []
        if turnedOn == 0:
            return res
        
        minutes = [0, 1, 2, 4, 8, 16, 32]
        hours = [0, 1, 2, 4, 8]
        def solve(h_used: list[int], m_used: list[int], h_sum: int, m_sum: int):

            if len(h_used) + len(m_used) == turnedOn:
                res.append([h_sum, m_sum])
                return
            
            if len(h_used) + len(m_used) > turnedOn:
                return
            

            for i in range(len(hours)):
                if hours[i] in h_used:
                    continue
                if h_sum + hours[i] > 11:
                    return
                h_used.append(hours[i])
                solve(h_used, m_used, h_sum + hours[i], m_sum)
                h_used.pop()
                for i in range(len(minutes)):
                    # if len(h_used) + i + 1 > turnedOn:
                    #     break
                    if minutes[i] in m_used:
                        continue
                    if minutes[i] + m_sum > 59:
                        break
                    m_used.append(minutes[i])
                    solve(h_used, m_used, h_sum, m_sum + minutes[i])
                    m_used.pop()
        solve([], [], 0, 0)
        return res
                # h_used.pop()


s = Solution()

print(s.readBinaryWatch(1))