import sys
import socket
import serial
global fs

def scpi_connect(host, port):
    global fs
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    sys.stderr.write("connected...")
    fs=s.makefile("rw")

def scpi_connect_serial(filename):
    global fs
    fs = serial.Serial(filename)
    sys.stderr.write("connected...")


def cmd(cmd_str):
    global fs
    sys.stderr.write(cmd_str+"\n")
    fs.write(str.encode(cmd_str))
    fs.write(str.encode("\r\n"))
    fs.flush()

def query(cmd_str):
    global fs
    cmd(cmd_str)
    line = fs.readline()
    sys.stderr.write(line.decode())
    return line.decode().strip('\n')
