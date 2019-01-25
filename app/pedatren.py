import requests, json, base64, sys
from requests.auth import HTTPBasicAuth
from app import logger

class Login():	
	# __url = 'https://api.pedatren.nuruljadid.app/'
	__url = 'http://207.148.75.98:3000/api/v1/'
	def __init__(self):
		try:
			open("token.txt", "r")
		except IOError:
			open("token.txt", "w")
		with open('token.txt', 'r') as f:
			token = f.read()
		self.__token = token
		self.__url = Login.__url 

	@property
	def headers(self):
		header = {
			'content-type' : 'application/json',
			'connection' : 'keep-alive',
			'User-Agent' : 'Penjaga POS NJ',
			'x-token' : self.token,
		}
		return header
	
	def setNewURL(self):
		self.__url = "http://api.pedatren.nj/"

	@property
	def url(self):
		return self.__url

	@property
	def urlpenjaga(self):
		return "{}{}".format(self.url,"penjagapos/perizinan/santri")

	def login(self, username=None, password=None):
		data = requests.get(self.url+'auth/login', auth=(username,password), headers=self.headers)
		if data.status_code == 200:
			self.__token = data.headers['x-token']
			with open('token.txt', 'w') as f:
				f.write(self.__token)
		return data.status_code
	
	def cekLogin(self):
		data = requests.get(self.url+'auth/login', headers = self.headers)
		return data.status_code

	@property
	def token(self):
		try:
			with open("token.txt", "r") as f:
				token = f.read()
		except:
			pass
		return token

	def level(self):
		user = self.token.split(".")[0]
		user += "=" * ((4 - len(user) % 4) % 4)
		level = json.loads(base64.b64decode(user))#['scope'][1]
		return level	

	def DecodeBASE64(self, Decode):
		dataToDECODE = Decode.split(".")[0]
		dataToDECODE += "=" * ((4 - len(dataToDECODE) % 4) % 4)
		hasils = json.loads(base64.b64decode(dataToDECODE))
		return hasils		

	@property
	def urlUser(self):
		lev = self.level()["scope"][1]
		print(lev)
		if 'penjagapos' in lev:
			urlUser = "{}penjagapos/".format(self.url)
		else:
			self.logOut()
			sys.exit(1)
		return urlUser

	@property
	def logOut(self):
		log = requests.get(self.url+'auth/logout', headers = self.headers).json()

class Pedatren(Login):

	def DetailIzin(self, idPerizinan):
		data = requests.get(self.urlpenjaga+"/{}".format(idPerizinan), headers=self.headers)
		data.close()
		return data

	def Keluar(self, idPerizinan):
		try:
			p = {"diketahui": "Y"}
			izin = requests.put(
				self.urlpenjaga+"/{}/pemberitahuan".format(idPerizinan),
				data=json.dumps(p), headers=self.headers
				)
			izin.close()
			print(izin.json())
			return izin.status_code
		except Exception as e:
			logger.exception(e)
			return 500
	
	def kembali(self, idPerizinan):
		try:
			p = {"kembali":"Y"}
			izin = requests.put(
				self.urlpenjaga+"/{}/statuskembali".format(idPerizinan),
				data=json.dumps(p),
				headers=self.headers
				)
			izin.close()
			print(izin.json())
			return izin.status_code
		except Exception as e:
			logger.exception(e)
			return 500

	def GetPerizinan(self, cari=None):
		try:
			datas = requests.get(
				self.urlpenjaga,
				params={"cari":cari},
				headers=self.headers)
			datas.close()
			if datas.status_code == 200:
				return json.loads(datas.content)
			elif datas.status_code == 403:
				return 403
		except Exception as e:
			logger.exception(e)