'''array=[5,7,21,9,11,17,1]
array2=list(set(array))
array2.sort()
print(array2)

print("Third highest number :",array2[-3])
print("Third highest number :",array2[-2])'''

#insertion sort
array=[5,7,21,9,11,17,1]
def insertion_sort(array):
    for i in range(1,len(array)):
        anchor=array[i]
        j=i-1
        while j>=0 and anchor<array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1] =anchor
array = [5, 7, 21, 9, 11, 17, 1]
insertion_sort(array)
print(array)



#bubblesort

def bubble_sort(array):
    size=len(array)

    for i in range(size-1):
       for j in range(size-1-i):
          if array[j]>array[j+1]:
              temporary= array[j]
              array[j]= array[j+1]
              array[j+1]=temporary


array=[5,7,21,9,11,17,1]
bubble_sort(array)
print(array)





#slection_sort

def selection_sort(array):
    size=len(array)
    for i in range(size-1):
        min=i
        for j in range(min+1,size):
            if array[j]<array[min]:
                min=j

        if i!=min:
            array[i],array[min]=array[min],array[i]
array=[5,7,21,9,11,17,1]
selection_sort(array)
print(array)
