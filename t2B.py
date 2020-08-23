
array = list() 
n = input("Enter the length of the array: ")  #this loop is for taking length of the array and printing array accordingly since 'a[i] = i' 

for j in range(int(n)): 
    
    array.append(j) #all the inputs are appended to the array so that the array of the form a[i] = i is formed.



queries = list() 
number = input("Enter the number of queries u want: ") 

for i in range(int(number)): 
    n = input("Enter in the following order 'startindex' 'endindex' 'value';  query {0}  :".format(i+1)) 
    queries.append(n)
    #this loop is to form of a list queries , so to access and use further


    
    test_str = queries[i]
    test_sub = " "
#since within the queries the inputs are separed by space, to get exact indices, we need to know the location of spaces and skip them    
    space = [m for m in range(len(test_str)) if test_str.startswith(test_sub, m)]
    # startswith string method searces for the sub string in the main string and 'm' is the start value and it iterates in the loop and provides all location of spaces
    a = space[0]
    b = space[1]
#accessing spaces locations
       

for k in range(0,len(queries)):
#iterating in the list of queries    
    
    startIndex = int(queries[k][0:a]) #storing starting index of each query
    endIndex = int(queries[k][a+1:b])#storing end index of each query
    value = int(queries[k][b+1: ])#storing value of each query

    z = array[startIndex:endIndex+1] #slicing the specified part of list for adding the given value in the query
    
    res = [x + value for x in z]    # using list comprehensions so as to add the given value to every 'i' in specified sliced list in the query
    
    array[startIndex:endIndex + 1] = res # replacing the result that is the list after adding value with original sliced list
    
    array = array[0:startIndex] + res + array[endIndex+1: ] # and finally concatinating all the parts that is head part , replaced list and trailing part.
    


        
print(max(array))  # and printing the maximum of resultant array which is formed undergoing all conditions as aforementioned and completing all iterations




"""
        TIME COMPLEXITY:
                n - for 1st loop
                n^2 - for 2nd loop #list comprehension for loop , looping inside
                n^2 - for 3rd loop # list comprehension for loop looping inside


                = n + 2n^2
                = O(n^2)

        SPACE COMPLEXITY:
                        IT depends on length of array + no. of queries
                        = n + n
                        = 2n
                        = O(n)
"""















