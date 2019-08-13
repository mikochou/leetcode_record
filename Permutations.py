#递归的方法。
    def dfs(self,nums,res,path):
        if not nums:
            res.append(path)
        else:
            for i in xrange(len(nums)):
                self.dfs(nums[:i]+nums[i+1:],res,path+[nums[i]])
    def permute(self, nums):
        res = []
        self.dfs(nums,res,[])
        return res
    
