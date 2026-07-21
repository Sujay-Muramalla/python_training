d = {'key1': 1, 'key2': 4, 'key3': 'bacon', 'key4': ['item0', 'item1', 'item2']}


new_list = []
for k, v  in d.items():
    print (k,v)
    
    if k=='key4':
       print (d[k])
       new_list = d[k].split(",")
       print ("new list: ", new_list)
       for item in new_list:
           print (item)
    


