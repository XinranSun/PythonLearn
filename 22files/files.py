import os.path

f = open("context.txt", "r")

# print(f.read(4))

# print(f.readline())
# print(f.readline()) == for line in f: print(line)

# for line in f:
#     print(line)
# f.close()

if not os.path.exists("sxr.txt"):
    f = open("sxr.txt", "x")
    print("File created")
    f.close()

if os.path.exists("sxr.txt"):
    os.remove("sxr.txt")
    print("File removed")
else:
    print("File exists")

with open("context.txt") as f:
    content = f.read()
if not os.path.exists("sxr.txt"):
    f = open("sxr.txt", "x")
    print("File created")
    f.close()
with open("sxr.txt","a") as f:
    f.write(content)