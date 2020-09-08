#pickle it
#demonstates pickling and shelving data

import pickle, shelve

print("pickling lists")
variety = ["sweet", "hot", "dill"]
shape = ["spear", "spade", "heart"]
brand = ["liandries", "rylais", "bullshit"]

f = open("pickles1.dat", "wb")
pickle.dump(variety, f, True)
pickle.dump(shape, f, True)
pickle.dump(brand, f, True)
#"true" unnessecary, but means stored in more efficient manner. Less human readable
f.close()

print("unpickling lists")
f = open("pickles1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print(brand)
f.close()

print("\nShelving lists")
s = shelve.open("pickles2.dat")
s["variety"] = ["sweet", "hot", "dill"]
s["shape"] = ["spear", "spade", "heart"]
s["brand"] = ["liandries", "rylais", "bullshit"]

s.sync()        #make sure data is written??

print("\nRetrieving thingies")
print("Brand -", s["brand"])
print("shape -", s["shape"])
print("Variety -", s["variety"])
s.close()
input()

