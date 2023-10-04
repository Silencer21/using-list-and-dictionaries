#import required modules
from pprint import pprint

#create outer list for all devices
devices = []

#open file and read list of device_info
file = open('devices-04.txt','r')
for line in file:
    #get device_info into list
    device_info_list = line.strip().split(',')
    #put device info into dictionary 
    device_info = {} #create inner dictionary of device_info
    device_info['name'] = device_info_list[0]
    device_info['os-type'] = device_info_list[1]
    device_info['ip'] = device_info_list[2]
    device_info['username'] = device_info_list[3]
    device_info['password'] = device_info_list[4]
#display 
    print('Read device information:', device_info)

#now append device and info into our devices list
    devices.append(device_info)





#display blank line
print('')

#display title
print('Input converted to list containing dictionaries:')

#display list
pprint(devices)

#close file
file.close()
