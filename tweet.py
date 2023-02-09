class Tweet:
    #prueba

    def __init__(self,fecha, usuario, recuperados,nuevosCasos,fallecidos,muestras,pcr,antigeno,totalRecuperados,totalCasos,totalFallecidos,totalMuestrasPorcesadas,totalActivos):
        self.fecha = fecha 
        self.usuario = usuario 
        self.recuperados = recuperados 
        self.nuevosCasos = nuevosCasos 
        self.fallecidos = fallecidos 
        self.muestras = muestras 
        self.pcr = pcr 
        self.antigeno = antigeno 
        self.totalRecuperados = totalRecuperados 
        self.totalCasos = totalCasos 
        self.totalFallecidos = totalFallecidos 
        self.totalMuestrasPorcesadas = totalMuestrasPorcesadas 
        self.totalActivos = totalActivos

    def toDBColecction(self):
        return{
            'fecha':self.fecha ,
            'usuario':self.usuario ,
            'recuperados':self.recuperados ,
            'nuevosCasos':self.nuevosCasos , 
            'fallecidos':self.fallecidos , 
            'muestras':self.muestras ,
            'pcr':self.pcr ,
            'antigeno':self.antigeno ,
            'totalRecuperados':self.totalRecuperados , 
            'totalCasos':self.totalCasos ,
            'totalFallecidos':self.totalFallecidos ,
            'totalMuestrasPorcesadas':self.totalMuestrasPorcesadas ,
            'totalActivos':self.totalActivos
        } 
    