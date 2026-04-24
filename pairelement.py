class pair_element:
    def twoSum(self,nums,target):
        lookup={}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num],i]
            lookup[num]=i
value=int(input("Enter the sum for which you want to make a search:"))
print("index1=%d,index2=%d" % int(pair_element().twoSum((10,20,30,40,50,60,70), value)))



        