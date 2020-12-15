# A Set of names
names = {"Steve", "Rick", "Negan"}
names2 = names

# adding a new element in the new set
names2.add("Glenn")

# removing an element from the old set
names.remove("Negan")


print("Old Set is:", names)
print("New Set is:", names2)

#############################


names_n = {"Steve", "Rick", "Negan"}

# copying using the copy() method
names2_n = names.copy()

# adding "Glenn" to the new set
names2_n.add("Glenn")

# removing "Negan" from the old set
names_n.remove("Negan")

# displaying both the sets
print("Old_n Set is:", names_n)
print("New_n Set is:", names2_n)

#################
