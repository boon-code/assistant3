""" pfpwd_ui.py --

 UI generated by GUI Builder Build 146 on 2009-04-02 12:38:17 from:
    /media/data/hubi/code/python/pfgui/pfpwd.ui
THIS IS AN AUTOGENERATED FILE AND SHOULD NOT BE EDITED.
The associated callback file should be modified instead.
"""

import Tkinter
import os # needed for relative image paths

# Using new-style classes: create empty base class object
# for compatibility with older python interps
#if sys.version_info < (2, 2):
#    class object:
#        pass

class Pfpwd(object):
    _images = [] # Holds image refs to prevent GC
    def __init__(self, root):


        # Widget Initialization
        self._frame_2 = Tkinter.Frame(root,
        )
        self._frame_3 = Tkinter.Frame(self._frame_2,
        )
        self._lsPwd = Tkinter.Listbox(self._frame_2,
            height = 0,
            width = 0,
        )
        self._butAdd = Tkinter.Button(self._frame_3,
            text = "add password",
        )
        self._entPwd = Tkinter.Entry(self._frame_3,
            width = 0,
        )
        self._butUpdate = Tkinter.Button(self._frame_3,
            text = "update",
        )

        # widget commands

        self._lsPwd.configure(
            xscrollcommand = self._lsPwd_xscrollcommand
        )
        self._lsPwd.configure(
            yscrollcommand = self._lsPwd_yscrollcommand
        )
        self._butAdd.configure(
            command = self._butAdd_command
        )
        self._entPwd.configure(
            invalidcommand = self._entPwd_invalidcommand
        )
        self._entPwd.configure(
            validatecommand = self._entPwd_validatecommand
        )
        self._entPwd.configure(
            xscrollcommand = self._entPwd_xscrollcommand
        )
        self._butUpdate.configure(
            command = self._butUpdate_command
        )


        # Geometry Management
        self._frame_2.grid(
            in_    = root,
            column = 1,
            row    = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_3.grid(
            in_    = self._frame_2,
            column = 1,
            row    = 2,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._lsPwd.grid(
            in_    = self._frame_2,
            column = 1,
            row    = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._butAdd.grid(
            in_    = self._frame_3,
            column = 2,
            row    = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 10,
            pady = 0,
            rowspan = 1,
            sticky = ""
        )
        self._entPwd.grid(
            in_    = self._frame_3,
            column = 1,
            row    = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 10,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self._butUpdate.grid(
            in_    = self._frame_3,
            column = 2,
            row    = 2,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 10,
            pady = 0,
            rowspan = 1,
            sticky = ""
        )


        # Resize Behavior
        root.grid_rowconfigure(1, weight = 0, minsize = 274, pad = 0)
        root.grid_columnconfigure(1, weight = 0, minsize = 373, pad = 0)
        self._frame_2.grid_rowconfigure(1, weight = 1, minsize = 40, pad = 0)
        self._frame_2.grid_rowconfigure(2, weight = 0, minsize = 40, pad = 0)
        self._frame_2.grid_columnconfigure(1, weight = 1, minsize = 40, pad = 0)
        self._frame_3.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_3.grid_rowconfigure(2, weight = 0, minsize = 40, pad = 0)
        self._frame_3.grid_columnconfigure(1, weight = 1, minsize = 40, pad = 0)
        self._frame_3.grid_columnconfigure(2, weight = 0, minsize = 40, pad = 0)


