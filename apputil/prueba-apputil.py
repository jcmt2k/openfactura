from apputil import DBConfig
config = DBConfig('config.conf')
print config.getDicPara('app.')
config.insPara('app.nombre','Un nombre')
config.insPara('app.telefono','123456789')
config.insPara('app.dir','89')
config.setPara('app.dir','')
config.insPara('app.nombre','Otro nombre')
config.insPara('otraapp.dir', 'Otro valor')
print "app."
print config.getDicPara('app.')
print "otra"
print config.getDicPara()
