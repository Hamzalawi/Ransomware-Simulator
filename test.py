import os

dir = "test_dir"

for root, dirs, files in os.walk(dir):
    for f in files:
        print(f"root: {root}\n dirs:{dirs}\nfiles:{files}\n ")

print("____________________________________________test 2 _____________________________")
print("________________________________________________________________________________")

path = "/home/kali/ahmed.txt"
name,ext = os.path.splitext(path)
print(name)
print(ext)