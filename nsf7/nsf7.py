#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#Copyright nsfac Bolivia 2007
#vea el archivo licencia.txt para detalles de licencia
__doc__='''Estas son las clases utilizadas para generar el código
de control para las facturas del nuevo sistema de facturación
de acuerdo a los requerimientos de SIN en Bolivia
'''
__author__ = "Julio Cesar Mejia Teran <jcmt2k@gmail.com>"
__version__ = "0.1"
__date__ = "Date: 2007/12/20"
__copyright__ = "Copyright (c) 2007 JulioC"
__license__ = "GPL"
#import string
class CodControl:
	'''La Clase CodControl encierra todo el procedimiento para la
	generación del código de control.
	'''
	def __init__(self, numAuto, numFac, nit, fecTra, montoTra, llave):
		'''Constructor de la clase CodControl. Verifica los parametros
		de construcción de la clase.
		'''
		if self._esNumAuto(numAuto):
			self._numAuto = numAuto
		else:
			print "CodControl:init:Error en el número de autorización"
		if self._esNumFac(numFac):
			self._numFac = numFac
		else:
			print "CodControl:init:Error en el número de factura"
		if self._esNit(nit):
			self._nit = nit
		else:
			print "CodControl:init:Error en el número de NIT"
		fecTra = fecTra.replace("/","")
		if self._esFecha(fecTra):
			self._fecTra = fecTra
		else:
			print "CodControl:init:Error en la fecha de la transacción"
		montoTra = self._redondeo(montoTra)
		if self._esMonto(montoTra):
			self._montoTra = montoTra
		else:
			print "CodControl:init:Error en el monto de la transacción"
		if self._esLlave(llave):
			self._llave = llave
		else:
			print "CodControl:init:Error en la llave"
		#print "CodControl:init Finalizado"
	def _esNumAuto(self, num):
		'''Verifica si la cadena num realmente se trata de un número de
		autorización: hasta 15 dígitos y solo se permiten 0,1,2,3,4,5,6,7,8,9
		'''
		resultado = True
		if len(num) <= 15:
			for i, v in enumerate(num):
				if num[i] not in ["0","1","2","3","4","5","6","7","8","9"]:
					resultado = False
		else:
			resultado = False
		return resultado
	def _esNumFac(self, num):
		'''Verifica si la cadena num realmente se trata de un número de
		factura: hasta 12 dígitos y solo se permiten 0,1,2,3,4,5,6,7,8,9
		'''
		resultado = True
		if len(num) <= 12:
			for i, v in enumerate(num):
				if num[i] not in ["0","1","2","3","4","5","6","7","8","9"]:
					resultado = False
		else:
			resultado = False
		return resultado
	def _esNit(self, nit):
		'''Verifica si la cadena num realmente se trata de un número de
		NIT: hasta 12 dígitos y solo se permiten 0,1,2,3,4,5,6,7,8,9
		'''
		resultado = True
		if len(nit) <= 12:
			for i, v in enumerate(nit):
				if nit[i] not in ["0","1","2","3","4","5","6","7","8","9"]:
					resultado = False
		else:
			resultado = False
		return resultado
	def _esFecha(self, fecha):
		'''Verifica si la cadena fecha realmente se trata de una fecha:
		días entre 1 y 31, meses entre 1 y 12, finalmente años entre
		2000 y 2050
		'''
		resultado = True
		if len(fecha) == 8:
			anio = int(fecha[0:4])
			mes = int(fecha[4:6])
			dia = int(fecha[6:8])
			if (dia < 1) or (dia > 31):
				resultado = False
				print "CodControl:_esFecha:Error en el dia de la fecha"
			elif (anio < 2000) or (anio > 2050):
				resultado = False
				print "CodControl:_esFecha:Error en el año de la fecha"
			elif (mes < 1) or (mes > 12):
				resultado = False
				print "CodControl:_esFecha:Error en el mes de la fecha"
		else:
			resultado = False
		return resultado
	def _esMonto(self, monto):
		'''Verifica si la cadena monto realmente se trata de un número:
		hasta 15 dígitos y solo se permiten 0,1,2,3,4,5,6,7,8,9
		'''
		resultado = True
		if len(monto) <= 15:
			for i, v in enumerate(monto):
				if monto[i] not in ["0","1","2","3","4","5","6","7","8","9"]:
					resultado = False
		else:
			resultado = False
		return resultado
	def _esLlave(self,llave):
		'''Verifica si la cadena llave realmente es un número de
		autorización: hasta 256 dígitos y solo se permiten los 
		caracteres que están en el diccionario dic.
		'''
		dic = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
		       "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", 
		       "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", 
		       "f", "g", "h", "i", "j", "k", "m", "n", "p", "q", 
		       "r", "s", "t", "u", "v", "w", "x", "y", "z", "2", 
		       "3", "4", "5", "6", "7", "8", "9", "=", "#", "(", 
		       ")", "*", "+", "-", "_", "\\", "@", "[", "]", "{", 
		       "}", "%", "$" ]
		resultado = True
		if len(llave) <= 256:
			for i, v in enumerate(llave):
				if llave[i] not in dic:
					resultado = False
		else:
			resultado = False
		return resultado
	def _redondeo(self,real):
		'''Provee el calculo del redondeo de acuerdo a la normativa del
		SIN: si la fracción es mayor o igual a 50 centavos, entonces se
		redondeará al entero inmediato superior.
		'''
		fReal = float(real)
		iReal = int(fReal)
		decimal = fReal - iReal
		if decimal >= 0.5:
			valor = iReal +1
		else:
			valor = iReal
		return str(valor)
	def _obtenerVerhoeff(self, cifra):
		'''Esta función obtiene el código de Verhoef de la cadena
		cifra pasada como Verifica si la cadena num realmente se trata de un número de
		autorización: hasta 15 dígitos y solo se permiten 0,1,2,3,4,5,6,7,8,9
		'''
		mul = [ [0,1,2,3,4,5,6,7,8,9],
		        [1,2,3,4,0,6,7,8,9,5],
		        [2,3,4,0,1,7,8,9,5,6],
		        [3,4,0,1,2,8,9,5,6,7],
		        [4,0,1,2,3,9,5,6,7,8],
		        [5,9,8,7,6,0,4,3,2,1],
		        [6,5,9,8,7,1,0,4,3,2],
		        [7,6,5,9,8,2,1,0,4,3],
		        [8,7,6,5,9,3,2,1,0,4],
		        [9,8,7,6,5,4,3,2,1,0] ]
		per = [ [0,1,2,3,4,5,6,7,8,9],
		        [1,5,7,6,2,8,3,0,9,4],
		        [5,8,0,3,7,9,6,1,4,2],
		        [8,9,1,6,0,4,3,5,2,7],
		        [9,4,5,3,1,2,6,8,7,0],
		        [4,2,8,6,5,7,3,9,0,1],
		        [2,7,9,3,8,0,6,4,1,5],
		        [7,0,4,6,9,1,3,2,5,8] ]
		inv = [0,4,3,2,1,5,6,7,8,9]
		check = 0
		numeroInvertido = []
		numeroInvertido[:] = cifra
		numeroInvertido.reverse()
		for i, v in enumerate(numeroInvertido):
			check = mul[check ][ per[((i+1) % 8)][int(numeroInvertido[i])]  ]
		return inv[check]
	def _cifrarMensajeRC4(self,mensaje, clave):
		'''Cifra el mensaje mensaje con la clave clave utilizando
		el algoritmos RC4
		'''
		#dic = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
		#		"K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
		#		"U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", 
		#		"e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
		#		"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", 
		#		"y", "z", "0", "1", "2", "3", "4", "5", "6", "7",
		#		"8", "9", "=", "#", "&", "(", ")", "*", "+", "-",
		#		"_", "/", "\\", "<", ">", "@", "[", "]", "{", "}",
		#		"%", "$" ]
		estado = range(256)
		x = 0
		y = 0
		indice1 = 0
		indice2 = 0
		nmen = 0
		mensajeCifrado = ""
		for i in range(256):
			indice2 = (ord(clave[indice1]) + estado[i] + indice2 ) % 256
			tmp = estado[i]
			estado[i] = estado[indice2]
			estado[indice2] = tmp
			indice1 = (indice1 + 1) % len(clave)
		for i in range(len(mensaje)):
			x = (x + 1) % 256
			y = (estado[x] + y) % 256
			tmp = estado[x]
			estado[x] = estado[y]
			estado[y] = tmp
			nmen = ord(mensaje[i]) ^ estado[(estado[x] + estado[y]) % 256] 
			mensajeCifrado = mensajeCifrado + (hex(nmen)[2:].rjust(2,"0"))
			#La siguiente línea convierte a hexadecimal y rellena con 0
			#(hex(nmen)[2:].rjust(2,"0"))
		return mensajeCifrado.upper()
	def _obtenerBase64(self,numero):
		'''Convierte el número numero a base 64, se basa en el
		diccionario definido en dic.
		'''
		dic = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
				"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
				"K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
				"U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", 
				"e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
				"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", 
				"y", "z", "+", "/" ]
		cociente = 1
		resto = 0
		palabra = ""
		while cociente > 0 :
			cociente = numero / 64
			resto = numero % 64
			palabra = dic[resto] + palabra
			numero = cociente
		return palabra
	def _pasoUno(self):
		'''Paso 1:
		Obtener y concatenar consecutivamente 2 dígitos Verhoeff al final
		de los siguientes datos: Número Factura, NIT/CI del Cliente,
		Fecha de la Transacción y Monto de la Transacción. Posteriormente
		hallar la sumatoria de los datos obtenidos y sobre este resultado
		generar consecutivamente 5 dígitos Verhoeff. Para efectos de 
		Verhoeff, tomar en cuenta el 0 (cero) como cualquier otro número,
		aún cuando este se encuentre a la izquierda de la cifra.
		'''
		self._numFac = self._numFac + str(self._obtenerVerhoeff(self._numFac))
		self._numFac = self._numFac + str(self._obtenerVerhoeff(self._numFac))
		self._nit = self._nit + str(self._obtenerVerhoeff(self._nit))
		self._nit = self._nit + str(self._obtenerVerhoeff(self._nit))
		self._fecTra = self._fecTra + str(self._obtenerVerhoeff(self._fecTra))
		self._fecTra = self._fecTra + str(self._obtenerVerhoeff(self._fecTra))
		self._montoTra = self._montoTra + str(self._obtenerVerhoeff(self._montoTra))
		self._montoTra = self._montoTra + str(self._obtenerVerhoeff(self._montoTra))
		intSuma = int(self._numFac) + int(self._nit) + int(self._fecTra) + int(self._montoTra)
		self._suma = str(intSuma)
		largo = len(self._suma)
		self._suma = self._suma + str(self._obtenerVerhoeff(self._suma))
		self._suma = self._suma + str(self._obtenerVerhoeff(self._suma))
		self._suma = self._suma + str(self._obtenerVerhoeff(self._suma))
		self._suma = self._suma + str(self._obtenerVerhoeff(self._suma))
		self._suma = self._suma + str(self._obtenerVerhoeff(self._suma))
		self._5verhoeff = self._suma[largo:]
	def _pasoDos(self):
		'''Paso 2
		Tomando cada uno de los 5 dígitos Verhoeff obtenidos, recuperar
		de la Llave de Dosificación 5 cadenas adyacentes, cada una con
		un largo definido por el dígito Verhoeff correspondiente más 1.
		Concatenar la primera cadena obtenida al final del dato
		relacionado al Número de Autorización; la segunda al Número de
		factura; la tercera al NIT/CI del Cliente; la cuarta a la Fecha
		de la Transacción y la quinta al Monto de la Transacción.
		'''
		llave = self._llave
		largo = eval(self._5verhoeff[0]) +1
		self._numAuto = self._numAuto + llave[:largo]
		llave = llave[largo:]
		largo = eval(self._5verhoeff[1]) +1
		self._numFac = self._numFac + llave[:largo]
		llave = llave[largo:]
		largo = eval(self._5verhoeff[2]) +1
		self._nit = self._nit + llave[:largo]
		llave = llave[largo:]
		largo = eval(self._5verhoeff[3]) +1
		self._fecTra = self._fecTra + llave[:largo]
		llave = llave[largo:]
		largo = eval(self._5verhoeff[4]) +1
		self._montoTra = self._montoTra + llave[:largo]
		llave = llave[largo:]
	def _pasoTres(self):
		'''Paso 3
		Aplicar el AllegedRC4 a la cadena conformada por la
		concatenación de todos los datos anteriores, utilizando como
		llave la concatenación de la Llave de Dosificación y los 5
		dígitos Verhoeff generados previamente.
		'''
		cad = self._numAuto + self._numFac + self._nit +self._fecTra + self._montoTra
		clave = self._llave + self._5verhoeff
		self._cifrado = self._cifrarMensajeRC4(cad, clave)
	def _pasoCuatro(self):
		'''Paso 4
		Obtener la sumatoria total de los valores ASCII de todos los
		caracteres de la cadena resultante del paso anterior, además,
		calcular 5 sumatorias parciales de los ASCII de ciertos
		caracteres de la misma cadena, de acuerdo al siguiente criterio:
		La primera sumatoria parcial tomará las posiciones 1,6,11,16,
		21, etc.; la segunda 2,7,12,17,22, etc.; la tercera 3,8,13,18,
		23, etc.; la cuarta 4,9,14,19,24, etc. y la quinta 5,10,15,20,
		25, etc.
		'''
		self._sumaTotal = 0
		self._suma1 = 0
		self._suma2 = 0
		self._suma3 = 0
		self._suma4 = 0
		self._suma5 = 0
		for i in range(len(self._cifrado)):
			self._sumaTotal = self._sumaTotal + ord(self._cifrado[i])
			if (((i+1)-1) % 5) == 0:
				self._suma1 = self._suma1 + ord(self._cifrado[i])
			if (((i+1)-2) % 5) == 0:
				self._suma2 = self._suma2 + ord(self._cifrado[i])
			if (((i+1)-3) % 5) == 0:
				self._suma3 = self._suma3 + ord(self._cifrado[i])
			if (((i+1)-4) % 5) == 0:
				self._suma4 = self._suma4 + ord(self._cifrado[i])
			if (((i+1)-5) % 5) == 0:
				self._suma5 = self._suma5 + ord(self._cifrado[i])
	def _pasoCinco(self):
		'''Paso 5
		Obtener las multiplicciones entre la sumatoria total y cada una
		de las sumatorias parciales. Dividir cada uno de los resultados
		obtenidos entre el dígito Verhoeff correspondiente más 1, el
		resultado deberá ser truncado. Finalmente obtener la sumatoria
		de todos los resultados y aplicar Base64.
		'''
		#print "CodControl:_pasoCinco:Iniciado"
		res1 = (self._sumaTotal * self._suma1) / (int(self._5verhoeff[0]) +1)
		res2 = (self._sumaTotal * self._suma2) / (int(self._5verhoeff[1]) +1)
		res3 = (self._sumaTotal * self._suma3) / (int(self._5verhoeff[2]) +1)
		res4 = (self._sumaTotal * self._suma4) / (int(self._5verhoeff[3]) +1)
		res5 = (self._sumaTotal * self._suma5) / (int(self._5verhoeff[4]) +1)
		self._resTotal = res1 + res2 + res3 + res4 + res5
		self._resTotal64 = self._obtenerBase64(self._resTotal)
		#print "CodControl:_pasoCinco:Finalizado"
	def _pasoSeis(self):
		'''Paso 6
		Aplicar el AllegedRC4 a la anterior expresión obtenida,
		utilizando como llave la concatenación de LLave de Dosificación
		y los 5 dígitos Verhoeff generados anteriormente.
		Adicionalmente se inserta el separador "-" cada dos caracteres.
		'''
		llave = self._llave + self._5verhoeff
		self._cc = self._cifrarMensajeRC4(self._resTotal64, llave)
		ccformato = ""
		for i in range(len(self._cc)):
			if ((i) % 2) == 0:
				ccformato = ccformato + "-"
			ccformato = ccformato + self._cc[i]
		self._cc = ccformato[1:]
	def getCodControl(self):
		'''Realiza los seis pasos para generar el código de control,
		llama a las funciones consecutivamentes de la uno a la seis.
		'''
		self._pasoUno()
		self._pasoDos()
		self._pasoTres()
		self._pasoCuatro()
		self._pasoCinco()
		self._pasoSeis()
		return self._cc
	def imprime(self):
		'''Imprime los atributos de la clase. Este método será retirado.
		'''
		print "NumAuto=" + self._numAuto
		print "NumFac=" + self._numFac
		print "Nit=" + self._nit
		print "FecTra=" + self._fecTra
		print "MontoTra=" + self._montoTra
		print "Llave=" + self._llave
		print "Verhoeff=" + self._5verhoeff
		print "cadena=" + self._cifrado
		print "sumaTotal=" + str(self._sumaTotal)
		print "resTotal=" + str(self._resTotal)
		print "resTotal64=" + self._resTotal64
		print "CodControl=" + self._cc
