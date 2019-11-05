message = ' Hello World '
print(message.rstrip().lstrip().lower())

myList = ['test2','test1','test3']
print('Before sort:' + str(myList))
myList.sort()
print('After sort:' + str(myList))
print('Last Element: ' + myList[-1])

myList.append('test4')
myList.insert(1, 'test5')
poppedElement = myList.pop(1)
myList.remove('test1')

print('Final:' + str(myList))


for i in myList:
    print('element: ' + i)

sliceTest = ['a','b','c','d','e']
print(sliceTest[1:4])

tupleTest = ('a','b','c','d','e')
print(tupleTest[1])



