# 13. Roman to Integer
class Solution {
    public int romanToInt(String s) {
        String rom = "IVXLCDM";
        int[] arr = {1, 5, 10, 50, 100, 500, 1000};
        int i = 0, n = 0;

        while (i < s.length() - 1)
        {
            if (s.charAt(i) == 'I' && (s.charAt(i + 1) == 'V' || s.charAt(i + 1) == 'X'))
            {
                n += arr[rom.indexOf(s.charAt(i + 1))] - arr[rom.indexOf(s.charAt(i))];
                i += 2; 
            }
            else if (s.charAt(i) == 'X' && (s.charAt(i + 1) == 'L' || s.charAt(i + 1) == 'C'))
            {
                n += arr[rom.indexOf(s.charAt(i + 1))] - arr[rom.indexOf(s.charAt(i))];
                i += 2; 
            }
            else if(s.charAt(i) == 'C' && (s.charAt(i + 1) == 'D' || s.charAt(i + 1) == 'M'))
            {
                n += arr[rom.indexOf(s.charAt(i + 1))] - arr[rom.indexOf(s.charAt(i))];
                i += 2;
            }
            else
            {
                n += arr[rom.indexOf(s.charAt(i))];
                i++;
            }
        }

        return i == s.length() ? n : n + arr[rom.indexOf(s.charAt(i))];
    }
}