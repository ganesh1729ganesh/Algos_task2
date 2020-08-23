expre_array = list() 
number = input("Enter the number of test cases you want to test:") #to store no. of test cases 
print ('Enter the expressions in terms of "<" and ">"  for testing') 
for i in range(int(number)): 
    n = input("Expression {0} :".format(i+1)) # to take all the inputs as expressions and form them as list of strings made of '<' and '>'
    expre_array.append(n) # appending all the inputs strings to form the list of expressions given for further access


less = '<'
great = '>'
dp = '<>'
bp = '><'
lp = '<<'
gp = '>>'
count = 0

for i in range(0,len(expre_array)):# iterating over the strings given in input
    for j in range(0,i+1):
        if expre_array[j][0] == less: # first index of the expression must be a '<' to be valid
            x = expre_array[j].count(less) # to find no. of '<'
            y = expre_array[j].count(great) # to find n0. of '>'
            if x == y:
                if expre_array[j][-2: ] == bp : # if both are equal the only exception case is string ending with '><' , so we need to trim that part to be valid
                    expre_array[j] = expre_array[j][0:-2]            
                    count = len(expre_array[j])
                else:
                    count = len(expre_array[j]) #other wise length of the prefix is = length of given string
                                  

            elif x != y: # if both no. of '<' and '>' are different
                
                test_str = expre_array[j]
                test_sub1 = less
                test_sub2 = great
                # the core idea is to find both the indices of '>' and '<' 

                
                lessIndices = [m for m in range(len(test_str)) if test_str.startswith(test_sub1, m)] #startswith method searches for mentioned value and returns indices of all its occurences
                greatIndices = [m for m in range(len(test_str)) if test_str.startswith(test_sub2, m)]

                if len(lessIndices) < len(greatIndices):
                # difference in the positions of the less and great
                
                    diffe = [greatIndices[i]- lessIndices[i]  for i in range(len(lessIndices))]
                    
                elif len(lessIndices) > len(greatIndices):
                    diffe = [greatIndices[i]- lessIndices[i]  for i in range(len(greatIndices))]
                    
                # the logic is for a uneqal no. of '<' and'>' , the differences in their indices is always an odd number to be valid
                for i in diffe:
                    
                    if i % 2!= 0:
                        
                        count = len(diffe)*2

                
                        
                        
                        
                       
        else:
            count = 0
    print("The length of the longest prefix upto which it is valid is: ",count)

"""
    TIME COMPLEXITY:
        `n - first for loop
         n^2(2n + 2n + n) = n^3
         n^3 + n
         = n^3 = O(n^3)
    SPACE COMPLEXITY:
        it depends on no. of test cases
        = O(n)   """








    
            
            
