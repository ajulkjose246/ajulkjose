import shutil
import os
# #copytree
# source_directory=r'C:\xampp\htdocs\mongo'
# destination_directory=r'D:\mathew\mongocopy'
# result=shutil.copytree(source_directory,destination_directory)
# print("Destination path:", result) 

# # copy
# source_directory=r'C:\xampp\htdocs\mongo\display.php'
# destination_directory=r'D:\roh\mongocopy\display_copy.php'
# print("the copied file is ",shutil.copy(source_directory,destination_directory))

# #moving
# source_directory=r'D:\roh\DVR.py'
# destination_directory=r'D:\roh\sys admins\DVR.py'
# shutil.move(source_directory,destination_directory)

# # removing  directory or file
# destination_directory=r'D:\mathew\mongocopy'
# (shutil.rmtree(destination_directory))

#details
# path=r'D:\mathew'
# print(shutil.disk_usage(path))

# #archiving
# r_path = r'D:\mathew'
# b_path=None
# Arch = "archive1"  
# print("succesfully created",shutil.make_archive(Arch, 'zip', root_dir=r_path, base_dir=b_path, verbose=0))

#  file and dir options
# print(shutil.which('python',mode=os.F_OK | os.X_OK, path=None))
# copy 2
source_path='C:\xampp\htdocs\mongo\display.php'
destination_path=r'D:\roh\mongocopy\display_copy2.php'
shutil.copy2(source_path, destination_path)