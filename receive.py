#!/usr/bin/python3
# UDP socket multicasting - receive with socketserver
# 12/11/17
# updated 6/7/18

# code below taken directly from python docs
# https://docs.python.org/3.4/library/socketserver.html

import socketserver


class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        socket.sendto(data.upper(), self.client_address)


if __name__ == '__main__':
    hostport = ('', 9999)
    server = socketserver.UDPServer(hostport, MyUDPHandler)
    print('listening for UDP broadcast messages...\n')
    server.serve_forever()
