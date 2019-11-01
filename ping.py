from pythonping import ping

host = '192.168.1.1'
host2 = '192.168.1.1'

size = 1
count = 1

file = open('ping.txt', 'w')

x = 1
y = '1'

for i in range(255):
    print(host2)

    response = ping(host2, size=size, count=count)

    file.write(host2)
    file.write('\n')
    file.write(str(response))
    file.write('\n')
    file.write('\n')

    x += 1
    y = str(x)

    host2 = host[:10] + y

file.close()
