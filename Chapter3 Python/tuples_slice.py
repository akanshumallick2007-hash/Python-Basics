#slice.tuple_tup[starting_idx:ending_idx]
#ending_idx is not included
tup=(2,1,4,1,3)
print(type(tup),len(tup),tup[1:3],tup)
#type, length, slicing
print(tup[1:4]) #in positive it's start with [0]
print(tup[:4])
print(tup[1:])
print(tup[2])
print(tup[-1:-4]) #in negative it's start from [-1]