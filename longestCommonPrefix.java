// 14. Longest Common Prefix

class Solution {
    public String longestCommonPrefix(String[] strs) {
        String s = strs[0];
        int start = 0, end = s.length(), i = 1;
        boolean flag = true;
        while (start <= end)
        {
            while (i < strs.length)
            {
                flag = true;
                if (!strs[i].startsWith(s.substring(start, end)) )
                {
                    flag = false;
                    break;
                }
                i++;
            }
            if (flag)
                return  s.substring(start, end);
            end--;
        }
        return "";
    }
}