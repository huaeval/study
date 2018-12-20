
#list and tuple
list2  = [0,1,2,3]
list1 = [3,2,1,0]

print list2 + list1

tuple1 = tuple(list1)
# tuple1[1] = 3
print tuple1

tuple2 = (1,2,3,4)
tuple3 = (6,)

tuple4 = tuple2 + tuple3
print tuple4

list3 = list(tuple4)

list3[0] = 'hi'

print list3

#1.list
list4 = [1,2]

print cmp(list4,[1,2])
print cmp(list4,[2,2])
print cmp(list4,[0,2])
print cmp(list4,["0",2])


print type(1) is int
