class Counter:    
    counter = 0

    def __init__(self):
        Counter.counter+=1
    
s1 = Counter()
s2 = Counter()
s3 = Counter()
s4 = Counter()
print(Counter().counter)


# Using call 
# class Counter:    
#     counter = 0
#     def __call__(self):
#         Counter.counter+=1
    
# s1 = Counter()
# s2 = Counter()
# s3 = Counter()
# s4 = Counter()
# s1()
# s2()
# s3()
# s4()
# print(Counter.counter)