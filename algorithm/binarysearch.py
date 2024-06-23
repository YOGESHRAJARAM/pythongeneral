# defining a functoin bainry search
def binary_search(arr,x):
    #defining variables
    low=0
    high=len(arr)-1
    
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<x:
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
        else:
            return mid
    # while the program comes to this part it have no resule
    return-1

   



arr=[46, 113, 126, 158, 166, 180, 186, 189, 221, 221, 232, 275, 311, 330, 349, 371, 377, 414, 455, 479, 479, 486, 492, 519, 525, 542, 567, 606, 612, 625, 627, 638, 647, 681, 731, 768, 785, 812, 814, 853, 853, 906, 926, 927, 938, 940, 962, 963, 965, 988]
x=46
result=binary_search(arr,x)

if result!=-1:
    print("the result is "+str(x)+" in the index of : " + str(result))
else:
    print("not in the arr")
