class Solution {
    public String rle(String s)
    {
        int i = 0, count = 0;
        StringBuilder sb = new StringBuilder(0);
        char c = s.charAt(0);
        while (i < s.length())
        {
            if (c == s.charAt(i))
            {
                count++;
                i++;
            }
            else 
            {
                sb.append(String.valueOf(count));
                sb.append(c);
                count = 0;
                c = s.charAt(i);
            }
        }
        sb.append(String.valueOf(count));
        sb.append(c);
        return sb.toString();
    }
    public String countAndSay(int n) {
        int i = 1;
        String s = "1";
        while (i < n)
        {
            s = rle(s);
            i++;
        }
        return s;
    }
}