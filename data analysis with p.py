my_list=[1,2,3]
print("original list:",my _list)
my_list.append(4)
print{"list after adding an element:", my_list}
my_list.remove(2)
print("list after removing an element:",my_list)
my_list[0]=10
print("list after adding an element:",my_list)
my_dict=('a':1,'b':2,'c':3)
print("\noriginal dictionary:",my_dict)
my_dict['d']=4
print("dictinary after adding an element:",my_dict)
del my_dict['b']
print("dictionary after removing an element:",my_dict)
my_dict['a']=10
print("dictionary after modifying an element:",my_dict)
my_set={1,2,3}
print("\noriginal set:",my_set)
my_set.add(4)
print("set after adding an element:",my_set)
my_set.remove(2)
print("set after removing an element:",my_set)
my_set.remove(1)
my_set.add(10)
print("set after modifying an element:",my_set)