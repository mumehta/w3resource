from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/home/munish') if isfile(join('/home/munish', f))]
print(files_list);