expre_array = list() 
number = input("Enter the number of test cases you want to test:") #to store no. of test cases 
print ('Enter the expressions in terms of "<" and ">"  for testing') 
for i in range(int(number)): 
    n = input("Expression {0} :".format(i+1)) # to take all the inputs as expressions and form them as list of strings made of '<' and '>'
    expre_array.append(n) # appending all the inputs strings to form the list of expressions given for further access


for i in range(len(expre_array)):
    count = 0
    suum = 0
    # iterating over the strings given in input
    for j in range(len(expre_array[i])):
                   
                
                    if expre_array[i][j] == '<' :
            #increasing sum by  '1'  for every '<' 
                       suum += 1

                    else:
                        suum -= 1  # decreasing sum by 1 for every '>'


                    if suum < 0:# expression starting with '>' case
                        break

                    if suum == 0:
                        count = j +1# so upto the maximum length of the expression that is valid the sum will be zero , so the index +1 gives the length of the valid sting
            

    print(count)

"""
        TIME COMPLEXITY:
                        since 2 loops one inside other + 1 input loop
                        = O(n^2)

        SPACE COMPLEXITY:

                        it depends on no. test cases and expressions
                        its based on input array
                        = O(n) """
