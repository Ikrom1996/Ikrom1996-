# iter_object = [12, 23, 1, 2, 2]
# my_list=iter(iter_object)
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
#
# class MyIterator:
#     def __init__(self,start,end):
#         self.start=start
#         self.end=end
#         self.current=start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current==self.end:
#             raise StopIteration
#         self.current+= 1
#         return self.current -1
#
#
# my_iterator=MyIterator(0,10)
# for i in my_iterator:
#     print(i)
#
# def range(start,end):
#     while start <= end:
#         yield start
#         start+= 1
#
# iter=range(0,10)
# print(next(iter))
# print(next(iter))
# print(next(iter))
#
#
# for i in range(0,10):
#         print(i)