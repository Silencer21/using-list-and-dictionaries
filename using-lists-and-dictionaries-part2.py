#import pprint required module
from pprint import pprint

#create device_info list
device_info = []

#open file and read single line of file
file = open('devices-03.txt', 'r')
file_line = file.readline().strip()

#display contents from the file
print('Read line: ',file_line)

#put contents of file into list
#use split function to convert
#comma seperates string into list of items
device_info = file_line.split(',')

#display a blank line to read
print('')

#display a title
print('Input converted to a list:')

#display the list with nice formatting
pprint(device_info)

#close file
file.close()
