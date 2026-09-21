class Solution {
    public int[] merge(int[] n1, int[] n2)
    {
        int i = 0, j = 0, k = 0;
        int[] res = new int[n1.length + n2.length];
        while (k < (res.length / 2) + 1)
        {
            if (i == n1.length)
                res[k++] = n2[j++];
            else if (j == n2.length)
                res[k++] = n1[i++];
            else
                res[k++] = n1[i] < n2[j] ? n1[i++] : n2[j++];
        }
        return res;
    }
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] res = merge(nums1, nums2);
        System.out.println(res.length / 2);
        return res.length % 2 == 0 ? 
            (res[res.length / 2] + res[(res.length / 2) - 1]) / 2.0 :
            res[res.length / 2];
    }
}