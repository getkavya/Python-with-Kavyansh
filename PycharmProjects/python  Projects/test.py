var1 = "kavi" 
var = "maheshwari"

with open("Test.txt", "a") as f:
    f.write(f"name - {var1}\n")
    f.write(f"surname {var}")
    f.close()