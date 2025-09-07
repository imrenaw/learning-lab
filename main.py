f = open("ml_data.txt", "x")
f.write("\nPython")
f.write("\nNumpy")
f.write("\nPandas")

with open("ml_data.txt", "r") as f:
    for line in f:
        print(line)
