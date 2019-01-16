from netmiko import ConnectHandler


arista_device = {
    'device_type': 'arista_eos',
    'ip': '192.168.122.10',
    'username': 'admin',
    'password': 'arista',
    'port': 22,
    'secret': 'arista',  # this is the enable password
    'verbose': True
}

connection = ConnectHandler(** arista_device)

if not connection.check_enable_mode():
    connection.enable()



with open('arista1_config.txt') as config:
    commands = config.read().splitlines()
# print(commands)

output = connection.send_config_set(commands)
print(output)


connection.disconnect()