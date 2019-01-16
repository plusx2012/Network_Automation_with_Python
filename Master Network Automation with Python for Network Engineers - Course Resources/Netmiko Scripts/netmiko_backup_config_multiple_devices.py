from netmiko import ConnectHandler
with open('devices.txt') as f:
        devices = f.read().splitlines()


for ip in devices:
    cisco_device = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': 'u1',
            'password': 'cisco',
            'port': 22,
            'secret': 'cisco',
            'verbose':True
            }
    print('Connecting to ' + ip)
    connection = ConnectHandler(**cisco_device)

    print('Entering enable mode ...')
    connection.enable()


    output = connection.send_command('show run')
    #print(output)

    prompt = connection.find_prompt()
    #print(prompt)
    hostname = prompt[:-1]
    #print(hostname)


    list = output.split('\n')
    list = list[3:]
    config = '\n'.join(list)
    #print(config)

    import datetime
    now = datetime.datetime.now()
    today = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    file = today + '-' + hostname + '.txt'




    with open(file + '.txt', 'w') as backup:
        backup.write(config)
        print('Backup of ' + hostname + ' completed successfully')
        print('#' * 30)

    connection.disconnect()