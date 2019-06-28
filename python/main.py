from data_structures import linked_list as list

list = list.LinkedList()
list.add(2)
list.add(10)
list.add(15)
list.add(12)
list.list()
print("Size " + str(list.len()))
list.delete(10)
list.list()
print("Size " + str(list.len()))
