#Write a function that gets a list of integers as a parameter.
#except that all uneven numbers have been removed.
#print out both the original as well as the cut-down list.
def ins(list):
    n = []
    for i in list:
        end = i % 2
        if end == 0:
            n.append(i)
            print(i)
    return n


number_list = [1,2,3,4,5,6,7,8,9,10]
m = ins(number_list)
print(number_list)
print(m)