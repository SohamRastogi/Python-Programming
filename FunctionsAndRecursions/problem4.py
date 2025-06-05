n = int(input("enter a number : "))

def sum_function(nums) : 
    if(nums==0) :
        return 0 
    return nums + sum_function(nums-1)

ans = sum_function(n)

print("the answer is : ",ans)