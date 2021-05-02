import os

print(os.getcwd())
if os.path.isfile("./41/task.txt"):
    print("Task.txt exists")
else:
    print("Task.txt does not exists")
