# Introduction to Sets
def average(array):
    # your code goes here
    s = set(array)
    return sum(s)/len(s)

arr = [86,45,13,248,654,65,54,6]
print(average(arr))

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)