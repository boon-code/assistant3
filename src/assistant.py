#!/usr/bin/env python

from Tkinter import *

from pfmain import CustomPfmain
from pfadd import CustomPfadd
from pfpwd import CustomPfpwd

import sys
import socket
import threading
import time

import platform

CONFIG_HOST = 'nimmermehr.local'
CONFIG_CMDPORT = 10030
CONFIG_MSGPORT = CONFIG_CMDPORT + 1
DEFAULT_READ_SIZE = 10
WAIT_TIME = 5
DEFAULT_SOCK_READ = 10
DEFAULT_BLOCK_TIME = 5.0
NOTIFY_TIME = 4000
USE_PYNOTIFY = False

if platform.system() == 'Windows':
    print "ohh... windows... naja..."
    CONFIG_HOST = CONFIG_HOST.strip('.local')

def global_report(msg):
    print msg

try:
    if not USE_PYNOTIFY:
        raise Exception("don't use pynotify")
    
    import pynotify
    if not pynotify.init("pfgui"):
        raise Exception("init notify failed")
    
    def global_report(msg):
        notify = pynotify.Notification("pfgui", msg)
        notify.set_timeout(NOTIFY_TIME)
        notify.show()
        print msg
    
except:
    pass

def create_client():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((CONFIG_HOST, CONFIG_CMDPORT))
    return sock

class application(object):
    
    def __init__(self):
        
        self._main_tk = Tk()
        # self will be passed
        self._main_gui = CustomPfmain(self._main_tk, self)
        self._main_tk.protocol('WM_DELETE_WINDOW', self.exit)
        self._scan_tk = None
        self._scan_gui = None
        self._pwd_tk = None
        self._pwd_gui = None
        self._lock = threading.RLock()
        self._ps = []
        self._thread = threading.Thread(target = self.__update_loop)
        self._thread.start()
        self.sendcmd('update')
    
    def mainloop(self):
        
        self._main_tk.mainloop()
        
    def __recv_msg(self, msg):
        
        msg = msg.split(' ', 1)
        if msg[0] == 'status':
            pn = msg[1].split('\n')
            self._lock.acquire()
            try:
                self._ps = pn
            finally:
                self._lock.release()
            
    def __update_loop(self):
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while 1:
            try:
                sock.connect((CONFIG_HOST, CONFIG_MSGPORT))
                break
            except (socket.gaierror, socket.error, socket.herror):
                time.sleep(WAIT_TIME)
                continue
        
        recv_buf = sock.recv(DEFAULT_READ_SIZE)
        buffer = ''
        while recv_buf != '':
            buffer += recv_buf
            pos = buffer.find('\n\n')
            if pos != -1:
                self.__recv_msg(buffer[:pos])
                buffer = buffer[pos + 2:]
            
            recv_buf = sock.recv(DEFAULT_READ_SIZE)
    
    def read_ps(self):
        
        self._lock.acquire()
        try:
            ps = self._ps
            return ps
        finally:
            self._lock.release()
    
    def show_scan(self):
        
        if self._scan_tk is None and self._scan_gui is None:
            self._scan_tk = Tk()
            self._scan_tk.protocol('WM_DELETE_WINDOW', self.close_scan)
            self._scan_gui = CustomPfadd(self._scan_tk, self)
            
            self._scan_tk.mainloop()
        
    def close_scan(self):
        
        self._scan_tk.quit()
        self._scan_tk.destroy()
        self._scan_tk = None
        self._scan_gui = None
    
    def show_pwd(self):
        
        if self._pwd_tk is None and self._pwd_gui is None:
            self._pwd_tk = Tk()
            self._pwd_tk.protocol('WM_DELETE_WINDOW', self.close_pwd)
            self._pwd_gui = CustomPfpwd(self._pwd_tk, self)
            
            self._pwd_tk.mainloop()
    
    def close_pwd(self):
        
        self._pwd_tk.quit()
        self._pwd_tk.destroy()
        self._pwd_tk = None
        self._pwd_gui = None
        
    def report(self, msg):
        
        global_report(msg)
    
    def sendcmd(self, data):
        
        print "sending: " + str(data)
        try:
            sock = create_client()
            sock.send(data + "\n\n")
            buffer = ''
            recv_buffer = sock.recv(DEFAULT_SOCK_READ)
            while recv_buffer != '':
                buffer += recv_buffer
                recv_buffer = sock.recv(DEFAULT_SOCK_READ)
            return buffer
        except:
            return "connection-error"
    
    def exit(self):
        
        self._main_tk.quit()
        sys.exit()

if __name__ == "__main__":
    root = application()
    root.mainloop()
