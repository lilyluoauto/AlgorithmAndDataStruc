#!/usr/bin/python
# -*- coding：utf-8 -*-
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-02-27 14:34
# IDE: PyCharm
# =========================================================
import time

import numpy as np

class LeetcodeSolution(object):

    ###rotate array
    # 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
#  示例 1:
#
#  输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
#
#  示例 2:
#
#  输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
#
#  说明:
#
#
#  尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
#  要求使用空间复杂度为 O(1) 的 原地 算法。
#
#  Related Topics 数组

    def RotateArray(self,nums,k):
        '''
        :param nums: List (int)
        :param k: int
        :return: None
        '''
        st=time.time()
        if k> len(nums):
            k=k-len(nums)
        s2=s[len(nums)-k:]
        s2.extend(nums[:k])
        for idx,itr in enumerate(s2):
            nums[idx]=itr
        # output=np.array(s2)
        ed=time.time()
        print("diff time:",ed-st)

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # s2=nums[len(nums)-k:]
        # s2.extend(nums[0:len(nums)-k])
        # nums=s2
        # # print("input is {}\noutput is {}".format(nums, s2))
        # print(nums)
        #reverse the array
        # for i in range(k):
        #     a = nums[i]
        #     nums[i] = nums[len(nums)- 1 - i]
        #     nums[len(nums)- i - 1] = a
        # print(nums)
        # for i in range(int((len(nums)-k)/2)):
        #     a = nums[k+i]
        #     nums[k+i]=nums[len(nums)-1-i]
        #     nums[len(nums)-1-i]=a
        # for i in range(int(k/2)):
        #     a=nums[i]
        #     nums[i]=nums[k-i-1]
        #     nums[k-i-1]=a
        # print(nums)
        # nums.reverse()
        # for i in range(int(len(nums)/2)):
        #     a=nums[i]
        #     nums[i]=nums[len(nums)-1-i]
        #     nums[len(nums)-1-i]=a
        #
        # for i in range(int(k/2)):
        #     a=nums[i]
        #     nums[i]=nums[k-1-i]
        #     nums[k-1-i]=a
        # for i in range(int((len(nums)-k)/2)):
        #     a=nums[k+i]
        #     nums[k+i]=nums[len(nums)-1-i]
        #     nums[len(nums)-1-i]=a
        st=time.time()
        self.ReverseArray(nums,0)
        if k>len(nums):
            k=k-len(nums)
        self.ReverseArray(nums,k,'start')
        self.ReverseArray(nums,k)
        ed=time.time()
        print(nums)
        print("diff time:",ed-st)
        # count=0
        # for i in range(k):
        #     a = nums[-1]
        #     j=len(nums)-1
        #     while j>0:
        #         nums[j]=nums[j-1]
        #         j-=1
        #         count+=1
        #     nums[0]=a
        # print(count)
        # for i in range(k):
        #     a=nums[-1]
        #     for j in range(len(nums)-1,0,-1):
        #         nums[j] = nums[j - 1]
        #     nums[0]=a




    def ReverseArray(self,nums,k,direction='end'):
        if direction=='start':
            for i in range(int(k/2)):
                a = nums[i]
                j=k-1-i
                if(j>=len(nums)):
                    break
                nums[i] = nums[k - 1 - i]
                nums[k - 1 - i] = a
        else:
            for i in range(int((len(nums) - k) / 2)):
                a = nums[k + i]
                nums[k + i] = nums[len(nums) - 1 - i]
                nums[len(nums) - 1 - i] = a




if __name__=="__main__":
    # s=np.linspace(1,10,10,endpoint=True)
#     # RotateArray(s,5)

    s=[1,2,3]
    # ,4,5,6,7,8,9,10]
    # s=[-1]
    # ,-100,3,99]
    k=4
    solution=LeetcodeSolution()
    # solution.rotate(s,k)
    solution.RotateArray(s,k)
    print(s)




