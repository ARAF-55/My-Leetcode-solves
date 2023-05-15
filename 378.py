# binary search in different fashion
import bisect

jaka = [1, 4, 5, 5, 7, 9, 11, 13, 34, 123, 144]
print(bisect.bisect_right(jaka, 10))

l = 1
r = 144

val = 9

while l < r:
    mid = (l + r) // 2
    if mid < val:
        l = mid + 1
    else:
        r = mid
print(r)
