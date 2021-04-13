#dictionary is nothing but key value pairs
d1={}
#print(type(d1))
d2={"Kavi":"pizza",
    "Rohan":"Fish", "Megha":"Roti",
    "shubham":{"B":"maggie", "L":"roti", "D":"chicken"}}#we can add dictionary in dictionary
#print(d2["Kavi"])#it will print what kavi eats.
#d2["Ankit"]="Junk Food"#it will add the person and what it eats.
#d2["Aurangzeb"]="Kebabs"#it will add the person and what it eats.
#del d2["Aurangzeb"]#this will delete that person from dict.
#print(d2["shubham"]["B"])
d3=d2.copy()
del d3 ["Kavi"]
print(d2)

