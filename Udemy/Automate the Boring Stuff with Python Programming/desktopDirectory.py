import os

os.chdir('C:\\Users\\jmsie\\Desktop')

for filename in os.listdir():
    if filename.endswith('.rxt'):
        #os.unlink(filename)
        print(filename)
