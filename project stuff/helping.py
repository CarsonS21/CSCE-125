list1 = ["Carson", 1, 2]
list2 = ["Nate", 3, 4]
list3 = ["Josh", 5, 6]

listoflists = [list1] + [list2] + [list3]

print(listoflists)
name = input("enter your name: ")
def find_name(listoflists, name):
    j = 0
    newlist = []
    for i in listoflists:
        if name in i:
            newlist = listoflists.pop(j)
            return newlist
        elif name not in i:
            j+= 1
            continue
    if name in newlist:
        return newlist
    else:
        newlist = [name, 0, 0, 0, 0]
        return newlist


nlist = find_name(listoflists, name)
print(nlist)
nlist[1] += 1
print(nlist)
