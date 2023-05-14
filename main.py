import os
import platform

print(os.name)
print(os.sep)
print(platform.uname())

# os.makedirs('New_folder') # making new folder


print(os.getcwd())  # print excisting directory

# wallk into director and her folder and filee
current_dir = os.getcwd()
print(os.walk(current_dir))

for item in os.walk(current_dir):
    print(item)

# changing directory
current_dir = os.getcwd()
print(current_dir)

# os.chdir('C:\\Users\\user.LAPTOP\\Desktop\\OS Module\\New_folder')

current_dir = os.getcwd()
print(current_dir)

print(os.stat('demo.txt'))

# creating new files in folder with the hep of join method
new_folder = os.path.join(current_dir, 'New_folder')
new_file = os.path.join(new_folder, 'index.html')

f = open(new_file, 'w')
f.write('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML 5 Boilerplate</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
	<script src="index.js"></script>
  </body>
</html>''')
# checking if any directory can exists with the help of os.path.exists method

# if not os.path.exists('dir_fol'):
#  os.makedirs('new_dir')


# spliting the filr
'''
current_fol = os.getcwd()

file_name =os.path.join(current_fol,'index.html')
print(os.path.split(file_name))
print(os.path.splitext(file_name))
'''

# rename the file name
'''
current_fol = os.getcwd()
filen_name = os.path.join(current_fol,'index.html')
print(os.rename(filen_name, 'home.html'))
'''

# copy paste file to one to another folder

'''

new_folder_path = os.path.join(current_dir, 'New_folder')
file_name = os.path.join(current_dir,'home.html')
print(os.rename(file_name,f"{new_folder_path}/ hom_e.html"))
'''''


# remove files
'''
file_name = os.path.join(current_dir,'home.txt')
print(os.remove(file_name))
'''
print(os.listdir())