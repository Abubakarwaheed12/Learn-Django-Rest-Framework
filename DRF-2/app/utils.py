
arr1 =[ ['00','01'], ['00','01'], ['00','01'], ['00','01'  ,  ['00','01'] ,  ['00','01',  ['00','01'] ,  ['00','01']] ,  ['00','01']] ,  ['00','01', ['00','01'], ['00','01'], ['00','01']],  ['00','01', ['00','01', ['00','01', ['00','01', ['00','01']]]]]]
l=[[[1,2,3],[1,2,3,4]],['23','32'],[3,5,6,],[{'key':2,'n1m':1}] , True]
        
def mularr(arr):
    flat=[]
    for i in arr:
        if type(i)==list:
            flat.extend(mularr(i))
        else:
            flat.append(i)
    return flat
                 

print(mularr(arr1))
    