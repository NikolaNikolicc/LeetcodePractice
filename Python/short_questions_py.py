# 1) list copy
list1 = [1, 2, 3, 4, 5]
list2 = list1
list1 = []
# what would be the output
print(list1)
print(list2)

# 2) define a function call in class's method in python and call it from the same method

class Solution:
    def method(self, param1):

        def innerMethod(param1):
            pass
            
        innerMethod(param1)
        
# 3) how many times len() will be calculated

while len(queue) > 0:
    # TODO some code
    pass

# answer: only one

# 4) What's the difference between hash set and hash map?

# answer: Hash set is list which don't have duplicates, hash map is hash set which have value for every value in list