#writing and appending a file
#f =open("kavyansh.txt", "w")
#a= f.write("kavi bhai bahut achhe hai\n")
#print(a)
#f.close()

#f =open("kavyansh2.txt", "a")
#a= f.write("kavi bhai bahut achhe hai\n")
#print(a)
#f.close()

#handle read and write both
f =open("kavyansh.txt", "r+")
print(f.read())
f.write("Thank You")