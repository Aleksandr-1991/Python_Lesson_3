print("\033[H\033[J", end="")

def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less  =  [i for i in array[1:] if i <= pivot] # Б-класть знач "i" проходясь по циклу "for i in array". Причём все эл.. после 1го.
    greater= [i for i in array[1:] if i > pivot]
    return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([1,5,6,8,59,47,68,98,26,29,4,71,5,48,3,7,67,52,8,63,7,2,12,47,69,73,97,85,5]))