d = {
    "key1": 1,
    "key2": 2,
    "key3": 3,
    "key4": [1,2,3,4]
}


for k,v in d.items():
    print (k,v)

    if k=="key4":
        print ("inside key4")
        print (d.get(k))
        print ("type of key4:", type(d.get(k)))
        d.get(k).append(5)
        d["key4"].append(199)
        d["key4"].extend([1,1,2,2,2,3])


for k,v in d.items():
    print (k,v)


print ("printing list comprehensions.. ")

lc = [x for x in range(1,10)]
print (lc)

print (sum(lc))
print (max(lc))








