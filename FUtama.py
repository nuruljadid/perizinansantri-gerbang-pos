# -*- coding: utf-8 -*-
#Boa:Frame:Frame1

import wx, detail
from wx.lib.anchors import LayoutAnchors
from app.pedatren import Pedatren
from app import logger
api = Pedatren()

# dw, dh = wx.DisplaySize()
# w, h = win.GetSize()
# print(w, h)
# print(dw, dh)

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTN_LOGOUT, wxID_FRAME1LC, wxID_FRAME1PANEL1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1TXT_BARCODE, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Frame1(wx.Frame):
    def _init_coll_lc_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading=u'Nama',
              width=340)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading=u'Domisili', width=370)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading=u'Lembaga', width=100)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading=u'Status Izin', width=200)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT,
              heading=u'Petugas Kamtib', width=450)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
            #   pos=wx.Point(158, 217), size=wx.Size(1145, 528),
              style=wx.DEFAULT_FRAME_STYLE | wx.CLOSE_BOX | wx.MAXIMIZE_BOX,
              title=u'Menu Utama')
        self.SetClientSize(wx.Size(1129, 490))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(1129, 490),
              style=wx.TAB_TRAVERSAL)

        self.txt_Barcode = wx.TextCtrl(id=wxID_FRAME1TXT_BARCODE,
              name=u'txt_Barcode', parent=self.panel1, pos=wx.Point(16, 40),
              size=wx.Size(400, 23), style=wx.TE_PROCESS_ENTER, value=u'')
        self.txt_Barcode.SetHint(u'Silahkan Scan Barcode')
        self.txt_Barcode.SetEditable(True)
        self.txt_Barcode.Show(True)
        self.txt_Barcode.SetConstraints(LayoutAnchors(self.txt_Barcode, True,
              True, False, False))
        self.txt_Barcode.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Segoe UI'))
        self.txt_Barcode.Bind(wx.EVT_TEXT_ENTER, self.OnTxt_BarcodeTextEnter,
              id=wxID_FRAME1TXT_BARCODE)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='staticText1', name='staticText1', parent=self.panel1,
              pos=wx.Point(16, 16), size=wx.Size(56, 16), style=0)

        self.lc = wx.ListCtrl(id=wxID_FRAME1LC, name=u'lc', parent=self.panel1,
            #   pos=wx.Point(12, 76), size=wx.Size(1091, 367),
            #   style=wx.LC_REPORT)
              style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.lc.Enable(False)
        self._init_coll_lc_Columns(self.lc)

        h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(h_sizer, 90, wx.EXPAND)
        sizer.Add(self.staticText1, 0, wx.ALL, 5)
        sizer.Add(self.txt_Barcode, 0, wx.ALL, 5)
        sizer.Add(self.lc, 3, wx.ALL | wx.EXPAND, 5)
        self.panel1.SetSizer(sizer)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.staticText1.SetLabel('''{}'''.format(api.level().get("nama_lengkap")))
        self.txt_Barcode.SetFocus()
        self.Center() # Set Center Frame
        self.Maximize(True)
        self.Tampilkan()
        self.TampilkanDetail("41")
            
    def Bersihkan(self):
        self.txt_Barcode.SetValue("")
        self.txt_Barcode.SetFocus()

    def TampilkanPesan(self, pesans):
        self.pesan = wx.MessageDialog(
            self,
            pesans,
            "Konfirmasi",
            wx.OK
        )
        self.Bersihkan()
        self.pesan.ShowModal()
    
    def PutPemberitahuan(self, idsantri, keluar=True):
        try:
            status = None
            if keluar:
                status = api.Keluar(idPerizinan=idsantri)
            if not keluar:
                status = api.kembali(idPerizinan=idsantri)
            self.Bersihkan()
            if status == 200:
                self.TampilkanDetail(idsantri)
            elif status == 400:
                self.TampilkanPesan("Gagal\nData perizinan ini sudah dilock, tidak bisa diupdate")
            elif status == 401:
                self.TampilkanPesan("Gagal\nLogin Kadaluarsa, Silahkan login kembali")
            elif status == 500:
                self.TampilkanPesan("Gagal\nKoneksi Tidak Stabil/Server Sedang Down. Silahkan Coba Lagi")
        except Exception as e:
            logger.exception(e)
        else:
            self.Tampilkan()
    
    def Tampilkan(self, cari=None):
        self.lc.DeleteAllItems()
        kolom = self.lc.GetItemCount()
        try:
            list_perizinan = api.GetPerizinan(cari=cari)
            for izin in list_perizinan:
                self.lc.InsertStringItem(kolom, izin.get("pemohon_izin").get("nama_lengkap"))
                self.lc.SetStringItem(kolom, 1, izin.get("pemohon_izin").get("domisili_santri"))
                self.lc.SetStringItem(kolom, 2, izin.get("pemohon_izin").get("lembaga") or "-")
                self.lc.SetStringItem(kolom, 3, izin.get("status_perizinan"))
                self.lc.SetStringItem(kolom, 4, izin.get("pemberitahuan_kamtib").get("nama_lengkap") or "-")
                kolom += 1   
        except Exception as e:
            logger.exception(e)


    def OnTxt_BarcodeTextEnter(self, event):
        if self.txt_Barcode.GetValue() == "":
            self.TampilkanPesan("Barcode Tidak Boleh Kosong")
        else:
            try:
                id_santri = api.DecodeBASE64(self.txt_Barcode.GetValue())
                tanya = wx.MessageDialog(None, "Set Perizinan Kembali Ke Pondok ?", "Konfirmasi", wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING)
                if tanya.ShowModal() == wx.ID_YES:
                    print("Ditampilkan")
                    self.PutPemberitahuan(id_santri.get("id_perizinan_santri"), keluar=False)
                else:
                    print("tidak ditampilkan")
                    self.PutPemberitahuan(id_santri.get("id_perizinan_santri"))
                self.Tampilkan()
            except Exception as e:
                self.TampilkanPesan("Silahkan Gunakan Barcode Yang Valid")
                logger.exception(e)

    def TampilkanDetail(self, idPerizinan):
        detail.id_izin = idPerizinan
        self.main = detail.create(None)
        self.main.Show()
