f = open("day7/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n","") for line in lines]

file_list = []
dir_list = []

for line in lines:
    split_line = line.split(" ")
    if split_line[0] == "$":
        if split_line[1] == "cd":
            if split_line[2] == "/":
                current_dir_list = []
            elif split_line[2] == "..":
                current_dir_list.pop()
            else:
                current_dir_list.append(split_line[2])
            new_dir = "/".join(current_dir_list)
            if new_dir not in dir_list:
                dir_list.append(new_dir)
    elif split_line[0] == "dir":
        continue
    else:
        new_file = ["/".join(current_dir_list) + split_line[1], int(split_line[0])]
        if new_file not in file_list:
            file_list.append(new_file)

total_files = sum([file[1] for file in file_list])
free_space = 70000000 - sum([file[1] for file in file_list])
required_space = 30000000
need_to_free = required_space - free_space

smallest_dir = total_files
for dir in dir_list:
    dir_size = 0
    for file in file_list:
        if file[0].startswith(dir):
            dir_size += file[1]
    if dir_size >= need_to_free and dir_size < smallest_dir:
        smallest_dir = dir_size

print(smallest_dir)