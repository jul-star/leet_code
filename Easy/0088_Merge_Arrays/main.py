
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        _res = []
        while i < m or j < n:
            if i == m:
                _res.append(nums2[j])
                j += 1
                continue
            if j == n:
                _res.append(nums1[i])
                i += 1
                continue

            if  nums1[i] < nums2[j]:
                  _res.append(nums1[i])
                  i += 1
            else:
                  _res.append(nums2[j])
                  j += 1
        nums1.clear()
        nums1.extend(_res)
        return nums1

def merge2(nums1: list[int], m: int, nums2: list[int], n: int)->list:
     i = m-1
     j = n-1
     k = m + n - 1
     while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
             nums1[k] = nums1[i]
             i -= 1
        else:
             nums1[k] = nums2[j]
             j -= 1
        k -= 1
     return nums1
        

def main():
    _res = merge2(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
    print(_res)
    assert _res == [1,2,2,3,5,6]

    _res = merge2(nums1 = [1], m = 1, nums2 = [], n = 0)
    print(_res)
    assert _res == [1]

    _res = merge2(nums1 = [0], m = 0, nums2 = [1], n = 1)
    print(_res)
    assert _res == [1]
    


if __name__ == '__main__':
      main()

                        
                
                