array = [1, 0, 3, 0, 0, 5, 7]
i=0 
for i in range(len(array)-1): 
    for index in range(len(array)-1): 
         if array[index]==0: 
            array[index+1], array[index]=array[index] ,array[index+1] 
print (array)  
