with open('devices.txt', 'r') as f:
    d = f.read().splitlines()

ip = list()
for item in d:
    x = item.split(':')
    ip.append(tuple(x))

print(ip)