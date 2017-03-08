def median(arr):
    arr.sort()
    if len(arr) %2 == 0:
        med = float(arr[len(arr)/2] + arr[len(arr)/2-1])/2
        return med
    return arr[(len(arr)-1)/2]
