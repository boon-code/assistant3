#!/usr/bin/env python
""" pfmain.py --

 UI generated by GUI Builder Build 146 on 2010-04-06 19:41:19 from:
    /media/data/hubi/code/python/pfgui3/pfmain.ui
 This file is auto-generated.  Only the code within
    '# BEGIN USER CODE (global|class)'
    '# END USER CODE (global|class)'
 and code inside the callback subroutines will be round-tripped.
 The 'main' function is reserved.
"""

from Tkinter import *
from pfmain_ui import Pfmain

# BEGIN USER CODE global
import tkMessageBox

UPDATE_TIME = 1000
# END USER CODE global

class CustomPfmain(Pfmain):
    pass

    # BEGIN CALLBACK CODE
    # ONLY EDIT CODE INSIDE THE def FUNCTIONS.

    # _butAdd_command --
    #
    # Callback to handle _butAdd widget option -command
    def _butAdd_command(self, *args):
        
		self._app.show_scan()

    # _butExit_command --
    #
    # Callback to handle _butExit widget option -command
    def _butExit_command(self, *args):
        
		self._app.exit()

    # _butHistory_command --
    #
    # Callback to handle _butHistory widget option -command
    def _butHistory_command(self, *args):
        
        self.__nmsg(self._app.sendcmd("history"))

    # _butKill_command --
    #
    # Callback to handle _butKill widget option -command
    def _butKill_command(self, *args):
        
        result = self._app.sendcmd("exit")
        self._app.report("trying to shutdown pfserver: " + result)
        self.__nmsg("trying to shutdown pfserver: " + result)

    # _butKillpacket_command --
    #
    # Callback to handle _butKillpacket widget option -command
    def _butKillpacket_command(self, *args):
        
        curr = self._lsPackets.curselection()
        if len(curr) > 0:
        	curr = curr[0]
        	name = self._lsPackets.get(curr)
        result = self._app.sendcmd('kill ' + name)
        self._app.report('starting packet processing: ' + result)
        self.__nmsg('starting packet processing: ' + result)

    # _butPwd_command --
    #
    # Callback to handle _butPwd widget option -command
    def _butPwd_command(self, *args):
    	
    	self._app.show_pwd()

    # _butResetsoft_command --
    #
    # Callback to handle _butResetsoft widget option -command
    def _butResetsoft_command(self, *args):
        
        curr = self._lsPackets.curselection()
        if len(curr) > 0:
        	curr = curr[0]
        	name = self._lsPackets.get(curr)
        result = self._app.sendcmd('reset ' + name)
        self._app.report('starting packet processing: ' + result)
        self.__nmsg('starting packet processing: ' + result)

    # _butShutdown_command --
    #
    # Callback to handle _butShutdown widget option -command
    def _butShutdown_command(self, *args):
        
        if tkMessageBox.askyesno("Shutdown Nimmermehr?", 
        		"Are you sure you want to shutdown Nimmermehr?"):
        	result = self._app.sendcmd('shutdown')
        	self._app.report('trying to shut down: ' + result)
        	self.__nmsg('trying to shut down: ' + result)

    # _butStart_command --
    #
    # Callback to handle _butStart widget option -command
    def _butStart_command(self, *args):
        
        curr = self._lsPackets.curselection()
        if len(curr) > 0:
        	curr = curr[0]
        	name = self._lsPackets.get(curr)
        result = self._app.sendcmd('start ' + name)
        self._app.report('starting packet processing: ' + result)
        self.__nmsg('starting packet processing: ' + result)

    # _butUpdate_command --
    #
    # Callback to handle _butUpdate widget option -command
    def _butUpdate_command(self, *args):
        
        result = self._app.sendcmd('update')
        self._app.report('requesting update: ' + result)
        self.__nmsg('requesting update: ' + result)

    # _lsPackets_xscrollcommand --
    #
    # Callback to handle _lsPackets widget option -xscrollcommand
    def _lsPackets_xscrollcommand(self, *args):
        pass

    # _sclPackets_command --
    #
    # Callback to handle _sclPackets widget option -command
    def _sclPackets_command(self, *args):
        pass

    # _txLog_xscrollcommand --
    #
    # Callback to handle _txLog widget option -xscrollcommand
    def _txLog_xscrollcommand(self, *args):
        pass

    # _txLog_yscrollcommand --
    #
    # Callback to handle _txLog widget option -yscrollcommand
    def _txLog_yscrollcommand(self, *args):
        pass

    # END CALLBACK CODE

    # BEGIN USER CODE class
    
    def __nmsg(self, msg):
    	self._txLog.delete('0.0', 'end')
    	self._txLog.insert('end', msg)
    
    def __amsg(self, msg):
    	self._txLog.insert('end', msg)
    
    def __update_packets(self, root):
    	
    	# update listbox
    	pstatus = self._app.read_ps()
    	if len(pstatus) > 0:
    		pstatus = [i.split(' ', 1) for i in pstatus]
    		lnames = self._lsPackets.get(0, 'end')
    		pnames = [i[0] for i in pstatus]
    		
    		ran = range(len(lnames))
    		ran.sort(reverse = True)
    		
    		for i in ran:
    			name = self._lsPackets.get(i)
    			if not name in pnames:
    				self._lsPackets.delete(i)
    		
    		for name in pnames:
    			if not name in lnames:
    				self._lsPackets.insert('end', name)
    		# update label
    		curr = self._lsPackets.curselection()
    		if len(curr) > 0:
    			curr = self._lsPackets.get(curr[0])
    			for i in pstatus:
    				if i[0] == curr:
    					self._labStatus.config(text = '\n  '.join(i))
    	
    	root.after(UPDATE_TIME, self.__update_packets, root)
	
    def __init__(self, root, app):

        Pfmain.__init__(self, root)
        self._app = app
        root.after(UPDATE_TIME, self.__update_packets, root)
        self._sclPackets["command"] = self._lsPackets.yview
    # END USER CODE class

def main():
    # Standalone Code Initialization
    # DO NOT EDIT
    try: userinit()
    except NameError: pass
    root = Tk()
    demo = CustomPfmain(root)
    root.title('pfmain')
    try: run()
    except NameError: pass
    root.protocol('WM_DELETE_WINDOW', root.quit)
    root.mainloop()

if __name__ == '__main__': main()
