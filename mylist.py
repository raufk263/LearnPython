"""
Lists are used to store multiple items in a single variable.
Lists are created using square brackets [] .
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.

--IMPORTANT FUNCTIONS IN LIST --
1. append() – Adds item to the end 
lst.append(3)

2. insert() – Adds item at specific index
lst = [1, 2]
lst.insert(1, 99)
# [1, 99, 2]


3. remove() – Removes first matching item
lst = [1, 2, 3]
lst.remove(2)
# [1, 3]

3. remove() – Removes first matching item

4. pop() – Removes and returns item at index

5. index() – Returns index of first match

6. count() – Counts occurrences of an item

7. sort() – Sorts the list
	list.sort()

8. reverse() – Reverses the list
	list.reverse()

9. copy() – Returns a copy of the list

10. clear() – Removes all items
---------------------------------------------------------
"""
DemoList = [1,3,4,2,5]
print(DemoList)

list2 = [1,2,3,'tea','coffee']
print(list2)
