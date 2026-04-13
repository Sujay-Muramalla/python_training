#file opening and reading operations
file = open(r"C:\Users\Lenovo\OneDrive\Backup_23102024\d_drive\PERSONAL\Career\Programming\Python\Udemy\Colt_Steele\bbc_requests_topics_2025-08-25.txt") 
x = file.read()
print (x)
 

filename="newsreads.txt"
with open(filename,"w") as file:
    file.write("------------BOF------------------------------")
    file.write(x)
    file.write("------------EOF-------------------------------")    
