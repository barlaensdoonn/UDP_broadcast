#!/usr/bin/python3
# UDP socket multicasting - simple send
# 12/11/17

import socket


hostport = ('', 9999)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(hostport)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.connect(('255.255.255.255', 9999))
sock.send('hello!\r\n'.encode())
