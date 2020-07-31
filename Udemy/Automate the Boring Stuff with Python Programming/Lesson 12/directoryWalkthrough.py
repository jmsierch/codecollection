import os

for foldername, subfolders, filenames in os.walk('c:\\My Games'):
    print('Folder Name: ' + foldername)
    print('Subfolder Names for ' + foldername + ': ' + str(subfolders))
    print('Filenames for ' + foldername + ': ' + str(filenames))
    print()

    for subfolder in subfolders:
        if 'fish' in subfolder:
            # os.rmdir(subfolder)
            print('rmdir on ' + subfolder)

    for file in filenames:
        if file.endswith('.xyz'):
            #shutil.copy(os.join(file, file), os.join(folderName, file + '.backup'))
            
