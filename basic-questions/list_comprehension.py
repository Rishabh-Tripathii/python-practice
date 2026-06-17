#Question: write a function that takes a list of numbers and returns only the even ones, using a list comprehension

def even(li):
    return [num for num in li if num%2==0]
li=list(map(int, input().split()))
print(even(li))