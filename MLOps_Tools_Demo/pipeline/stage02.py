with open("artifacts/sample.txt", "r") as f:
    s = f.read()
    print(s)

with open("artifacts/output.txt", "w") as f:
    f.write("HELLoooooo")