# -*- coding: utf-8 -*-
#Boa:MiniFrame:MiniFrame1

import wx, json
from threading import Timer
from app.pedatren import Pedatren
from app import logger
api = Pedatren()

id_izin = None

def create(parent):
    return MiniFrame1(parent)

[wxID_MINIFRAME1, wxID_MINIFRAME1LC, wxID_MINIFRAME1PANEL1, 
 wxID_MINIFRAME1STATICTEXT1, wxID_MINIFRAME1STATICTEXT11, 
 wxID_MINIFRAME1STATICTEXT13, wxID_MINIFRAME1STATICTEXT14, 
 wxID_MINIFRAME1STATICTEXT15, wxID_MINIFRAME1STATICTEXT16, 
 wxID_MINIFRAME1STATICTEXT2, wxID_MINIFRAME1STATICTEXT3, 
 wxID_MINIFRAME1STATICTEXT4, wxID_MINIFRAME1STATICTEXT5, 
 wxID_MINIFRAME1STATICTEXT6, wxID_MINIFRAME1STATICTEXT7, 
 wxID_MINIFRAME1STATICTEXT8, wxID_MINIFRAME1STATICTEXT9, 
 wxID_MINIFRAME1TXT_ALAMAT, wxID_MINIFRAME1TXT_ALASAN, 
 wxID_MINIFRAME1TXT_BERMALAM, wxID_MINIFRAME1TXT_BIKTREN, 
 wxID_MINIFRAME1TXT_DOMISILI, wxID_MINIFRAME1TXT_KAMTIB, 
 wxID_MINIFRAME1TXT_KETERANGAN, wxID_MINIFRAME1TXT_LAMA_IZIN, 
 wxID_MINIFRAME1TXT_LEMBAGA, wxID_MINIFRAME1TXT_NAMA_IZI, 
 wxID_MINIFRAME1TXT_NAMA_PEMBUAT_IZIN, wxID_MINIFRAME1TXT_NAMA_PENGANTAR, 
 wxID_MINIFRAME1TXT_PENGASUH, wxID_MINIFRAME1TXT_STATUS_IZIN, 
] = [wx.NewId() for _init_ctrls in range(31)]

class MiniFrame1(wx.MiniFrame):
    def _init_coll_lc_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading=u'NIS',
              width=200)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading=u'Nama Lengkap', width=300)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.MiniFrame.__init__(self, id=wxID_MINIFRAME1, name='', parent=prnt,
              pos=wx.Point(391, 258), size=wx.Size(1032, 539),
              style=wx.DEFAULT_FRAME_STYLE, title='Detail Perizinan Santri')
        self.SetClientSize(wx.Size(1016, 501))

        self.panel1 = wx.Panel(id=wxID_MINIFRAME1PANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(1016, 501),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_MINIFRAME1STATICTEXT1,
              label=u'Pemohon Izin', name='staticText1', parent=self.panel1,
              pos=wx.Point(16, 8), size=wx.Size(123, 26), style=0)
        self.staticText1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Segoe UI'))

        self.staticText2 = wx.StaticText(id=wxID_MINIFRAME1STATICTEXT2,
              label=u'Nama Lengkap', name='staticText2', parent=self.panel1,
              pos=wx.Point(16, 48), size=wx.Size(80, 16), style=0)

        self.staticText3 = wx.StaticText(id=wxID_MINIFRAME1STATICTEXT3,
              label=u'Alamat', name='staticText3', parent=self.panel1,
              pos=wx.Point(16, 80), size=wx.Size(38, 16), style=0)

        self.staticText4 = wx.StaticText(id=wxID_MINIFRAME1STATICTEXT4,
              label=u'Domisili Santri', name='staticText4', parent=self.panel1,
              pos=wx.Point(16, 112), size=wx.Size(76, 16), style=0)

        self.staticText5 = wx.StaticText(id=wxID_MINIFRAME1STATICTEXT5,
              label=u'Lembaga', name='staticText5', parent=self.panel1,
              pos=wx.Point(16, 140), size=wx.Size(49, 17), style=0)

        self.staticText6 = wx.StaticText(id=wxID_MINIFRAME1STATICTEXT6,
              label=u'Alasan Izin', name='staticText6', parent=self.panel1,
              pos=wx.Point(16, 230), size=wx.Size(56, 16), style=0)

        self.staticText7 = wx.StaticText(id=wxID_MINIFRAME1STATICTEXT7,
              label=u'Bermalam', name='staticText7', parent=self.panel1,
              pos=wx.Point(16, 169), size=wx.Size(54, 16), style=0)

        self.staticText8 = wx.StaticText(id=wxID_MINIFRAME1STATICTEXT8,
              label=u'Lama Perizinan', name='staticText8', parent=self.panel1,
              pos=wx.Point(16, 199), size=wx.Size(80, 16), style=0)

        self.staticText9 = wx.StaticText(id=wxID_MINIFRAME1STATICTEXT9,
              label=u'Keterrangan', name='staticText9', parent=self.panel1,
              pos=wx.Point(16, 262), size=wx.Size(64, 16), style=0)

        self.txt_nama_izi = wx.StaticText(id=wxID_MINIFRAME1TXT_NAMA_IZI,
              label=u'txt_nama_izin', name=u'txt_nama_izi', parent=self.panel1,
              pos=wx.Point(127, 48), size=wx.Size(71, 16), style=0)

        self.txt_alamat = wx.StaticText(id=wxID_MINIFRAME1TXT_ALAMAT,
              label=u'txt_alamat', name=u'txt_alamat', parent=self.panel1,
              pos=wx.Point(127, 80), size=wx.Size(54, 16), style=0)

        self.txt_domisili = wx.StaticText(id=wxID_MINIFRAME1TXT_DOMISILI,
              label=u'txt_domisili', name=u'txt_domisili', parent=self.panel1,
              pos=wx.Point(127, 112), size=wx.Size(60, 16), style=0)

        self.txt_lembaga = wx.StaticText(id=wxID_MINIFRAME1TXT_LEMBAGA,
              label=u'txt_lembaga', name=u'txt_lembaga', parent=self.panel1,
              pos=wx.Point(127, 140), size=wx.Size(64, 16), style=0)

        self.txt_bermalam = wx.StaticText(id=wxID_MINIFRAME1TXT_BERMALAM,
              label=u'txt_bermalam', name=u'txt_bermalam', parent=self.panel1,
              pos=wx.Point(128, 168), size=wx.Size(72, 16), style=0)

        self.txt_lama_izin = wx.StaticText(id=wxID_MINIFRAME1TXT_LAMA_IZIN,
              label=u'txt_lama_izin', name=u'txt_lama_izin', parent=self.panel1,
              pos=wx.Point(128, 199), size=wx.Size(67, 16), style=0)

        self.txt_alasan = wx.StaticText(id=wxID_MINIFRAME1TXT_ALASAN,
              label=u'txt_alasan', name=u'txt_alasan', parent=self.panel1,
              pos=wx.Point(128, 230), size=wx.Size(51, 16), style=0)

        self.txt_keterangan = wx.StaticText(id=wxID_MINIFRAME1TXT_KETERANGAN,
              label=u'txt_keterangan', name=u'txt_keterangan',
              parent=self.panel1, pos=wx.Point(128, 262), size=wx.Size(77, 16),
              style=0)

        self.staticText11 = wx.StaticText(id=wxID_MINIFRAME1STATICTEXT11,
              label=u'Pengantar', name='staticText11', parent=self.panel1,
              pos=wx.Point(568, 48), size=wx.Size(80, 16), style=0)

        self.txt_nama_pengantar = wx.StaticText(id=wxID_MINIFRAME1TXT_NAMA_PENGANTAR,
              label=u'txt_nama_pengantar', name=u'txt_nama_pengantar',
              parent=self.panel1, pos=wx.Point(720, 48), size=wx.Size(107, 16),
              style=0)

        self.staticText13 = wx.StaticText(id=wxID_MINIFRAME1STATICTEXT13,
              label=u'Pembuat Izin', name='staticText13', parent=self.panel1,
              pos=wx.Point(568, 80), size=wx.Size(80, 16), style=0)

        self.txt_nama_pembuat_izin = wx.StaticText(id=wxID_MINIFRAME1TXT_NAMA_PEMBUAT_IZIN,
              label=u'txt_nama_pembuat_izin', name=u'txt_nama_pembuat_izin',
              parent=self.panel1, pos=wx.Point(720, 80), size=wx.Size(124, 16),
              style=0)

        self.staticText14 = wx.StaticText(id=wxID_MINIFRAME1STATICTEXT14,
              label=u'Pengasuh', name='staticText14', parent=self.panel1,
              pos=wx.Point(568, 112), size=wx.Size(52, 16), style=0)

        self.txt_pengasuh = wx.StaticText(id=wxID_MINIFRAME1TXT_PENGASUH,
              label=u'txt_pengasuh', name=u'txt_pengasuh', parent=self.panel1,
              pos=wx.Point(720, 112), size=wx.Size(70, 16), style=0)

        self.staticText15 = wx.StaticText(id=wxID_MINIFRAME1STATICTEXT15,
              label=u'Biktren', name='staticText15', parent=self.panel1,
              pos=wx.Point(568, 140), size=wx.Size(37, 16), style=0)

        self.txt_biktren = wx.StaticText(id=wxID_MINIFRAME1TXT_BIKTREN,
              label=u'txt_biktren', name=u'txt_biktren', parent=self.panel1,
              pos=wx.Point(720, 140), size=wx.Size(55, 16), style=0)

        self.staticText16 = wx.StaticText(id=wxID_MINIFRAME1STATICTEXT16,
              label=u'Kamtib', name='staticText16', parent=self.panel1,
              pos=wx.Point(568, 168), size=wx.Size(38, 16), style=0)

        self.txt_kamtib = wx.StaticText(id=wxID_MINIFRAME1TXT_KAMTIB,
              label=u'txt_kamtib', name=u'txt_kamtib', parent=self.panel1,
              pos=wx.Point(720, 168), size=wx.Size(55, 16), style=0)

        self.txt_status_izin = wx.StaticText(id=wxID_MINIFRAME1TXT_STATUS_IZIN,
              label='staticText10', name=u'txt_status_izin', parent=self.panel1,
              pos=wx.Point(16, 288), size=wx.Size(119, 31), style=0)
        self.txt_status_izin.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Segoe UI'))

        self.lc = wx.ListCtrl(id=wxID_MINIFRAME1LC, name=u'lc',
              parent=self.panel1, pos=wx.Point(15, 328), size=wx.Size(505, 147),
              style=wx.LC_REPORT)
        self._init_coll_lc_Columns(self.lc)

    def __init__(self, parent):
        self._init_ctrls(parent)
        try:
            self.Tampilkan()
        except Exception as e:
            logger.exception(e)
        self.Center()

    def Tampilkan(self):
        datas = api.DetailIzin(id_izin)
        datas.close()
        datas = json.loads(datas.content)
        self.txt_nama_izi.SetLabel(datas.get("pemohon_izin").get("nama_lengkap"))
        self.txt_alamat.SetLabel(datas.get("pemohon_izin").get("alamat"))
        self.txt_domisili.SetLabel(datas.get("pemohon_izin").get("domisili_santri"))
        self.txt_lembaga.SetLabel(datas.get("pemohon_izin").get("lembaga"))
        self.txt_alasan.SetLabel(datas.get("alasan_izin"))
        self.txt_bermalam.SetLabel(datas.get("bermalam"))
        self.txt_lama_izin.SetLabel(datas.get("selama"))
        self.txt_keterangan.SetLabel(datas.get("keterangan") or "-")
        self.txt_status_izin.SetLabel(datas.get("status_perizinan"))
        # Pengantar
        self.txt_nama_pengantar.SetLabel(datas.get("pengantar").get("nama_lengkap") or "-")
        # Pembuat Izin
        self.txt_nama_pembuat_izin.SetLabel("{} | {}".format(
            datas.get("pembuat_izin").get("nama_lengkap") or "-",
            datas.get("pembuat_izin").get("status") or "-",
            ))
        # Pengasuh
        self.txt_pengasuh.SetLabel(datas.get("persetujuan_pengasuh").get("nama_lengkap") or "-")
        # Biktren
        self.txt_biktren.SetLabel(datas.get("persetujuan_biktren").get("nama_lengkap") or "-")
        # Kamtib
        self.txt_kamtib.SetLabel(datas.get("pemberitahuan_kamtib").get("nama_lengkap") or "-")
        if "anggota_rombongan" in datas:
            self.rombongan(datas.get("anggota_rombongan"))
    
    def rombongan(self, data_rombongan):
        self.lc.DeleteAllItems()
        kolom = self.lc.GetItemCount()
        for i in data_rombongan:
            self.lc.InsertStringItem(kolom, i.get("nis_santri"))
            self.lc.SetStringItem(kolom, 1, i.get("nama_lengkap"))
            kolom += 1
