#import required modules
from pprint import pprint

#create outer dictionary and lists
devices = {} #create outer dictionary for all OS-types
devices['ios'] = [] #create empty list of devices
devices['nx-os'] = [] #create empty list of devices
devices['ios-xr'] = [] #create empty list of devices

#open file and read list of device info
file = open('devices-04.txt','r')
for line in file:
    #get device info list
    device_info_list = line.strip().split()

    #put device info into dictionary 
    device_info = {} #create inner dictionary of device_info
    device_info['name'] = device_info_list[0]
    device_info['os-type'] = device_info_list[1]
    device_info['ip'] = device_info_list[2]
    device_info['username'] = device_info_list[3]
    device_info['password'] = device_info_list[4]

    #display
    print('Read device information: ',device_info)

    #place our device and its info into correct list of devices,
    #in main os-type dictionary based on device`s os-type
    devices[device_info['os-type']].append(device_info)

#display blank line
print('')

#display title 
print('Input converted to a dictionary with OS sorting:')

#display dictionary 
pprint(devices)

#close file
file.close()