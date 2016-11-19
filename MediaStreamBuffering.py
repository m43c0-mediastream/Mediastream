# -*- coding: UTF-8 -*-
from MediaStremSo.MediaStreamImports import *
	
class Buffering(object):
    def __init__(self, totalBytes, receivedBytes,NewDyrDownload,session):
        self.totalBytes = totalBytes
        self.receivedBytes = receivedBytes
        self.NewDyrDownload = NewDyrDownload
        self.session = session
          
    @property		                
    def ControlBuffering(self):
        KbTotaliDownload= KbScaricatiDownload= sectotali= temporimanete= secondiscaricati= MbBuffering = MbBufferingStart = secvisti = 0
        try:
          service = self.session.nav.getCurrentService()
          seek = service.seek()		  
          KbTotaliDownload = self.totalBytes / 1024 		  
          KbScaricatiDownload = int(self.receivedBytes)	/ 1024	
          sectotali = seek.getLength()[1]	/ 90000 	  
          secvisti = seek.getPlayPosition()[1] / 90000
          Mbs = KbTotaliDownload / sectotali		  
          secondiscaricati  =  KbScaricatiDownload / Mbs		  
          temporimanete = secondiscaricati - secvisti
          MbBuffering = (Mbs * 240 / 1024)  + (os.path.getsize(self.NewDyrDownload)/ 1024/ 1024)
          MbBufferingStart = float(os.path.getsize(self.NewDyrDownload))			
        except:
          pass
        return  KbTotaliDownload, KbScaricatiDownload, sectotali, temporimanete, secondiscaricati,MbBuffering,MbBufferingStart,secvisti
		
    @property		                
    def Controltime(self):		
        minution = minutioff = 5
        try:
          service = self.session.nav.getCurrentService()
          seek = service.seek()		  
          sectotali = seek.getLength()[1] /60	/ 90000 	  
          secvisti = seek.getPlayPosition()[1] / 60 / 90000	  	  
          minution = int(sectotali) - int(secvisti)	
          minutioff = int(sectotali) - minution
        except:
          pass
        return  minution, minutioff