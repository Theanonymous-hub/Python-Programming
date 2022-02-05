#You are given with two arrays .Your task is to merge the array such that first array is assending order and second is descending order.
#Input description
#First line contains two integer'n' and'm'.'n' denotes length of array 1 and 'm' of array 2.
#Next line contains 'm' space seperated numbers

a =input()
arr1 =list(map(int,input()))
arry2 =list(map(int,input()))
arr1.sort()
arr2.sort(reverse=True)
c = arr1*arr2
print(*c)
