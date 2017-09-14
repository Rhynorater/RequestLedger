#!/usr/bin/env python
#Logs HTTP Requests to the server. Designed for troubleshooting host header poisoning in recon

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser
import datetime
import socket

requestdate = datetime.datetime.today().strftime('%Y%m%d')
requestid = 0

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        global requestid
        requestid +=1
        request_path = self.path
        log = open("logfile.txt", "a")
        log.write("----- Incoming Request - Request ID "+str(requestdate)+"_"+str(requestid)+" ----->\n")
        log.write("Client Address:" + str(self.client_address[0])+"\n")
        log.write("Client Hostname:" + str(socket.gethostbyaddr(self.client_address[0])[0])+"\n")

        log.write("----- *Request Start* -----\n")
        log.write(request_path+"\n")
        log.write(str(self.headers))
        
        log.write("<----- *Request End* -----\n\n\n")
        self.send_response(200)
        #self.send_header("Set-Cookie", "foo=bar")
        
    def do_POST(self):
        global requestid
        requestid+=1
        request_path = self.path
        log.write("----- Incoming Request - Request ID "+str(requestdate)+"_"+str(requestid)+"----->\n")
        log.write("Client Address:" + str(self.client_address[0])+"\n")
        log.write("Client Hostname:" + str(socket.gethostbyaddr(self.client_address[0])[0])+"\n")
        log.write("----- *Request Start* -----\n")
        log.write(request_path+"\n")
        
        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0
        
        log.write(request_headers)
        log.write(self.rfile.read(length))
        log.write("<----- *Request End* -----\n\n\n")
        log.close()
        self.send_response(200)
    
    do_PUT = do_POST
    do_DELETE = do_GET
        
def main():
    port = 80
    #port=443
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()

        
