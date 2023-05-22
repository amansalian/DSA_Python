N = int(input('Enter the number of elements in the array: '))
list_1 = []

for i in range(0, N):
    element = int(input(f'Enter the {i} element: '))
    list_1.append(element)


print(list_1)


class Solution:
    def missingNumber(self,array_1,n):
        #Generate continuous numbers till N-1
        #list_2 = []
        #not_found = []
        #for i in range(0, n+1):
            #list_2.append(i)
        
        #for j in array_1:
            #for k in list_2:
                #if j != k:
                    #not_found.append(j)
        total = (n + 1)*(n)//2
        sum_of_A = sum(array_1)
        return total - sum_of_A
    

x = Solution()

print(x.missingNumber(list_1,N))
        


