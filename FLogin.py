# -*- coding: utf-8 -*-
#Boa:Frame:Frame1

import wx, FUtama, sys
from app.pedatren import Pedatren
api = Pedatren()

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTN_LOGIN, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1TXT_PASSWORD, 
 wxID_FRAME1TXT_USERNAME, 
] = [wx.NewId() for _init_ctrls in range(8)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(804, 317), size=wx.Size(426, 230),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Halaman Login')
        self.SetClientSize(wx.Size(410, 192))
        self.Center(wx.HORIZONTAL)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(410, 192),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Username', name='staticText1', parent=self.panel1,
              pos=wx.Point(40, 53), size=wx.Size(53, 16), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Password', name='staticText2', parent=self.panel1,
              pos=wx.Point(40, 101), size=wx.Size(50, 16), style=0)

        self.txt_Username = wx.TextCtrl(id=wxID_FRAME1TXT_USERNAME,
              name=u'txt_Username', parent=self.panel1, pos=wx.Point(136, 50),
              size=wx.Size(238, 23), style=wx.TE_PROCESS_ENTER, value=u'')
        self.txt_Username.Bind(wx.EVT_TEXT_ENTER, self.OnTxt_UsernameTextEnter,
              id=wxID_FRAME1TXT_USERNAME)

        self.txt_Password = wx.TextCtrl(id=wxID_FRAME1TXT_PASSWORD,
              name=u'txt_Password', parent=self.panel1, pos=wx.Point(136, 98),
              size=wx.Size(237, 23), style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER,
              value=u'')
        self.txt_Password.Bind(wx.EVT_TEXT_ENTER, self.OnTxt_PasswordTextEnter,
              id=wxID_FRAME1TXT_PASSWORD)

        self.btn_Login = wx.Button(id=wxID_FRAME1BTN_LOGIN, label=u'Login',
              name=u'btn_Login', parent=self.panel1, pos=wx.Point(176, 143),
              size=wx.Size(88, 26), style=0)
        self.btn_Login.Bind(wx.EVT_BUTTON, self.OnBtn_LoginButton,
              id=wxID_FRAME1BTN_LOGIN)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'APP Khusus Akun PENJAGA POS', name='staticText3',
              parent=self.panel1, pos=wx.Point(40, 8), size=wx.Size(325, 31),
              style=0)
        self.staticText3.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Segoe UI'))

    def __init__(self, parent):
        self._init_ctrls(parent)   
        self.txt_Username.SetFocus()
        status = api.cekLogin()
        self.Center()
        if status == 200:
              self.FrameUtama()
        # self.FrameUtama()

    def FrameUtama(self):
        self.main = FUtama.create(None)
        self.main.Show()
        self.Close()

    def TampilkanPesan(self, pesan):
        self.pesan = wx.MessageDialog(
            self,
            "{}".format(pesan),
            "Konfirmasi",
            wx.OK
        )
        self.pesan.ShowModal()

    def Bersihkan(self):
        self.txt_Username.SetValue("")
        self.txt_Password.SetValue("")
        self.txt_Username.SetFocus()
    
    def Login(self, username, password):
        status = api.login(username, password)
        if status == 401:
            self.TampilkanPesan("Username/Password Tidak Sesuai")
        elif status == 200:
            level = api.level().get("scope")[1]
            if level == "penjagapos":
                self.FrameUtama()
            else:
                self.TampilkanPesan("Hanya Boleh Menggunakan Akun PENJAGAPOS")
                api.logOut
                self.Bersihkan()
        else:
            self.TampilkanPesan("Jaringan Tidak Stabil")

    def OnTxt_UsernameTextEnter(self, event):
        if self.txt_Username.GetValue() == "":
            self.TampilkanPesan("Username Tidak Boleh Kosong")
            self.Bersihkan()
        else:
            self.txt_Password.SetFocus()

    def OnTxt_PasswordTextEnter(self, event):
        if self.txt_Password.GetValue() == "":
            self.TampilkanPesan("Password Tidak Boleh Kosong")
        else:
            self.Login(
                self.txt_Username.GetValue(),
                self.txt_Password.GetValue(),
            )

    def OnBtn_LoginButton(self, event):
        if self.txt_Username.GetValue() != "" and self.txt_Password.GetValue() != "":
            self.Login(
                self.txt_Username.GetValue(),
                self.txt_Password.GetValue(),
            )
