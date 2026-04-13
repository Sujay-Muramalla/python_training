
import time 

print("---------Time taken by Generator -------------")
gen_start_time = time.time()
print(sum(n for n in range(1,1000000)))
gen_time = time.time() -gen_start_time
print (gen_time)

print ("------------Time taken by list ---------------")
list_start_time = time.time()
print (sum([n for n in range(1,1000000)]))
list_time = time.time() - list_start_time
print (list_time)