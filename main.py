import os
from netstat import *
from sys import argv

temp_netstat_list = []
netstat_object_list = []
pid_set = set()


def main(port):
    netstat_list = os.popen("netstat -ano | findstr \"" + port + "\"").read().split(" ")

    for i in netstat_list:
        if '\n' in i:
            netstat_object_list.append(netstat(temp_netstat_list[0], temp_netstat_list[1], temp_netstat_list[2],
                                               temp_netstat_list[3], str(i).replace("\n", "")))
            pid_set.add(str(i).replace("\n", ""))
        elif i != '':
            temp_netstat_list.append(i)

    for i in netstat_object_list:
        print(i)

    msg_list = os.popen("taskkill /f /pid " + pid_set.pop()).read().split(" ")
    print(msg_list)


if __name__ == '__main__':
    main(argv[1])
