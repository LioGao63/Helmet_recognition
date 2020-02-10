import os

corr_file = []
files = []
path = "data/images"

corr_file = os.listdir(path)
# print(corr_file)
for file in corr_file:
    files.append(file)

# print(files)

label_path ="data/labels"

ofile = open("data/train.txt")

for line in ofile:
    line = line.split("/")[2].strip('\n')
    corr_file.append(line)

flist = list(set(files).difference(set(corr_file)))
print(len(flist))
print(flist)


