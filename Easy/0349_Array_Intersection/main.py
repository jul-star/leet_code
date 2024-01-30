class Solution:
    def insct(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))
    
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        if len(nums1) <= len(nums2):
            return self.intersect(nums1, nums2)
        else:
            return self.intersect(nums2, nums1)
    
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        l:list[int] = []     
        for i in range(len(nums1)):
            if nums1[i] in nums2 and \
            (len(l) == 0 or nums1[i] > l[len(l)-1]):
                l.append(nums1[i])
        return l
    
def main():
    s = Solution()
    l = s.intersection([2,1], [1,2])
    print(f'l: {l}')


if __name__ == '__main__':
    main()
