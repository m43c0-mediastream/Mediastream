# -*- coding: UTF-8 -*- 
from Moduli.MediaStremSo.MediaStreamImports import *
from Moduli.MediaStremSo.MediaStreamIptv import *
from Moduli.MediaStremSo.MediaStreamMain import *
from Moduli.MediaStremSo.MediaStreamCrypto import *
from Moduli.MediaStremSo.MediaStreamSfondo import *
from Moduli.MediaStremSo.MediaStreamJobs import *
from Moduli.MediaStremSo.MediaStreamSettingIptv import *

global jsession
jsession = None 
MediaStreamSettingSession = MainDownload(jsession)
MediaStreamPluginSession = MediaStreamPlugin(jsession)
MediaStreamLogo = iTimerLogo(jsession)
iMediaStreamIptv = iTimerIPtv(jsession) 
    
def sessionstart(reason, **kwargs):
    if ControlOnDsl():
      jsession = kwargs["session"]
      if reason == 0:	
        jm.resettostart()
        MediaStreamSettingSession.gotSession(jsession)
        iMediaStreamIptv.gotSession(jsession)
        MediaStreamPluginSession.gotSession(jsession)  
        MediaStreamLogo.gotSession(jsession)
		
MediaStreamSettingSession = MainDownload(jsession)  	  
MediaStreamPluginSession = MediaStreamPlugin(jsession)
MediaStreamLogo = iTimerLogo(jsession)	  
iMediaStreamIptv.gotSession(jsession)

def Main(session, **kwargs):
    if ControlOnDsl():
      session.open(MediaStreamMin)
    else:
      session.open(MessageBox,"Non risulta una connessione internet attiva, il plugin non puo funzionare..\n", MessageBox.TYPE_INFO, timeout = 20)
	  
def menu(menuid, **kwargs):
    if menuid == 'mainmenu':
        return [(Description_plug,Main,Description_plug,1)]
    return []
	
def Plugins(**kwargs):
    return [PluginDescriptor(name=Description_plug, description=Description_plug + ' ' + Version, icon='Panel/MediaStream.png', where=[PluginDescriptor.WHERE_EXTENSIONSMENU, PluginDescriptor.WHERE_PLUGINMENU], fnc=Main),
            PluginDescriptor(name=Description_plug, description=Description_plug + ' ' + Version, where=PluginDescriptor.WHERE_MENU, fnc=menu),
            PluginDescriptor(where=[PluginDescriptor.WHERE_SESSIONSTART], fnc=sessionstart)]
