import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()



#if name in namesOne, and same name in namesTwo
# what import helps here...
# duplicates = []
# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)
#OG runtime: 4.99112606048584 seconds O(n^2)
#improved runtime: runtime: 1.1109709739685059 secondsO(n log n)

# dictionary
duplicates = []
dictionary = {}
for name in names_1:
        dictionary[name] = 1
for name in names_2:
        if name in dictionary:
                #debug "unsubscriptable" means something is in brackets when it needs to be in parenthesis
                duplicates.append(name)
# very improved runtime: runtime: 0.004872322082519531 seconds O(n)

# duplicates = set(names_1) & set(names_2)
# this is why we use built-ins: runtime: 0.004230022430419922 seconds!!!!!!!!!!!!!!!!!!!!!!!!!


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


