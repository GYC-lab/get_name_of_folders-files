import os

# read names of files/folders and save them with lists 
# you can export results to markdown files and visualize them with a tree map(using a extension "markmap")

# locate files/folders
path = "D:\\OPTIMUS\\sft\\Program\\Fortran\\Others\\HIPSTAR\\PLATUS\\fortran\\source\\INCLUDE_ROM"

# get names of files/folders
datanames = os.listdir(path)
file_list = []
for name in datanames:
    file_list.append(name)

# record files/folders
path_sub = []
sub_file_name = []
sub_folder_name = []
num_name=len(datanames)
for i in range(num_name):
    path_sub.append(path +'\\' +file_list[i])
    if os.path.isdir(path_sub[i]):
        sub_folder_name.append(file_list[i])
    else:
        sub_file_name.append(file_list[i])

# sort names(folders -> files)
sorted_file_list = []
for name in sub_folder_name:
    sorted_file_list.append(name)
for name in sub_file_name:
    sorted_file_list.append(name)

# write names
filename="output_names.md"
textFile = open(filename,"w",encoding = "UTF-8") 
for name in sorted_file_list:
    textFile.write('- '+name+'\n')
textFile.close()


# features to be added 
# 1. search all names
# 2. textbf

