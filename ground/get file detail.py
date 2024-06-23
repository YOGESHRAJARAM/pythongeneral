import os

file = "test.py" # change this to your file name
size = os.path.getsize(file) # get the file size in bytes
mtime = os.path.getmtime(file) # get the last modified time in seconds
stat = os.stat(file) # get the stat_result object

print(f"File name: {file}")
print(f"File size: {size} bytes")
print(f"Last modified time: {mtime} seconds")
print(f"File mode: {stat.st_mode}")
print(f"File inode: {stat.st_ino}")
print(f"File device: {stat.st_dev}")
print(f"Number of hard links: {stat.st_nlink}")
print(f"User ID of owner: {stat.st_uid}")
print(f"Group ID of owner: {stat.st_gid}")
print(f"Time of last access: {stat.st_atime} seconds")
print(f"Time of last status change: {stat.st_ctime} seconds")