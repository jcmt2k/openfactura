import sys
import string
import nsf7

c = 0
f = open("5000CasosPruebaCCVer7.txt")
try:
	malos=0
	buenos=0
	for line in f:
		c = c + 1
		#print str(c) + "=" + line
		l = line.split("|")
		#print l
		a = nsf7.CodControl(l[0],l[1],l[2],l[3].replace("/",""),l[4].replace(",",".") ,l[5])
		codigo = a.getCodControl()
		#print str(c) + ":[" + l[10] + "]=[" + codigo +"]"
		if l[10] <> codigo:
			print "ERROR EN LA LINEA" + str(c)
			malos = malos +1
		else:
			buenos = buenos +1
	print "Buenos=", buenos
	print "Malos=", malos
finally:
	f.close()
