from netmiko import ConnectHandler

with open('devices.txt') as f:
    devices = f.read().splitlines()

device_list = list()
for ip in devices:
    cisco_device = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': 'andrei',
            'password': 'cisco',
            'port': 22,
            'secret': 'cisco', #this is the enable password
            'verbose': True
            }
    device_list.append(cisco_device)

#print(device_list)
for device in device_list:
    print('Connecting to ' + device['ip'])
    connection = ConnectHandler(**device)

    print('Entering enable mode ...')
    connection.enable()

    file = input('Enter configuration file (use a valid path) for ' + device['ip'] +':')

    print('Running commands from file:', file, 'to device:', device['ip'])
    output = connection.send_config_from_file(file)
    print(output)

    connection.disconnect()