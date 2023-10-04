#import pprint module
from pprint import pprint

#create list
device_info = {}

#open file and read single line
file = open('devices-03.txt', 'r')
file_line = file.readline().strip()

#display input from file
print('Read line: ', file_line)

#use the string split to convert
#comma seperates string into lists
device_info_list = file_line.split(',')

#put items from list into dictionary

device_info['name'] = device_info_list[0]
device_info['os-type'] = device_info_list[1]
device_info['ip'] = device_info_list[2]
device_info['username'] = device_info_list[3]
device_info['password'] = device_info_list[4]


#display blank line
print('')

#display title
print('Input converted to dictionary:')

#display dictionary
pprint(device_info)

#close file
file.close()


