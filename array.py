a =input()
arr1 =list(map(int,input()))
arry2 =list(map(int,input()))
arr1.sort()
arr2.sort(reverse=True)
c = arr1*arr2
print(*c)
