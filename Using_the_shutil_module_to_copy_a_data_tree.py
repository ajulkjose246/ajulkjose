import shutil
source_dir = './test'
destination_dir = './new'
shutil.copytree(source_dir, destination_dir)
print("Directory tree copied successfully!")

