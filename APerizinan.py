#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Boa:App:BoaApp

import wx

import FLogin

modules ={u'FLogin': [1, 'Main frame of Application', u'FLogin.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = FLogin.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
