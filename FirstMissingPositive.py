# 先遍历一遍原数组，将原数组中的1-n的整数存入哈希表对应0到n-1的位置。
再对哈希表进行遍历，遍历到存储内容为空的，则返回遍历到整数的索引值，即为第一个丢失的正整数。
      if nums == []:
            return 1

        n = len(nums)
        hashed = [0]*n
        for i in range(n):
            if nums[i]>0 and nums[i]<=n:
                hashed[nums[i]-1]+=1
        
        for i in range(n):
            if hashed[i]==0:
                return i+1
        return n+1
