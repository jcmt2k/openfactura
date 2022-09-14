#-*- encoding: utf-8 -*-
import anydbm
class DBConfig:
	'''Clase DBConfig
	Esta clase abstrae el almacenamiento de la configuración de una
	aplicación de manera persistente.
	'''
	def __init__(self, filename):
		'''Constructor de DBConfig
		El constructor inicializa las variables.
		'''
		self._archivo = filename
		db = anydbm.open(self._archivo,'c')
		db.close()
	def __del__(self):
		'''Destructor de DBConfig
		El destructor de la clase.
		'''
		pass
	def getPara(self, para):
		'''DBConfig:getPara(para)
		Este método obtiene el valor de un parámetro específico.
		'''
		db = anydbm.open(self._archivo,'c')
		return db[para]
		db.close()
	def setPara(self, para, valor):
		'''DBConfig:setPara(para, valor)
		Este método ajusta el valor de un parámetro específico.
		'''
		db = anydbm.open(self._archivo,'c')
		try:
			antes = db[para]
			db[para] = valor
		except:
			print "ERROR:DBConfig:setPara:El parámetro [",para,"] no existe"
		db.close()
	def getDicPara(self, suf=''):
		'''DBConfig:getListaPara(suf)
		Este método retorna un diccionario de los parámetro que
		empiezan con la cadena suf y sus valores. Si no sele da un
		parámetro, retorna un diccionario completo
		'''
		db = anydbm.open(self._archivo,'c')
		dic = []
		for k, v in db.iteritems():
			if (k.find(suf) == 0):
				dic.append({k:v})
		db.close()
		return dic
	def delPara(self, para):
		'''DBConfig:delPara(para)
		Este método borra un parámetro.
		'''
		db = anydbm.open(self._archivo,'c')
		try:
			del db[para]
		except:
			print "ERROR:DBConfig:delPara:El parámetro [",para,"] no existe"
		db.close()
	def insPara(self, para, valor):
		'''DBConfig:insPara(para, valor)
		Este método inserta un nuevo parámetro y su valor para ser
		almacenado.
		'''
		db = anydbm.open(self._archivo,'c')
		db[para] = valor
		db.close()
