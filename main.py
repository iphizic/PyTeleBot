from PyQt5 import QtCore, QtNetwork, QtWidgets
from PyQt5.QtNetwork import QNetworkAccessManager
from PyQt5.QtNetwork import QNetworkRequest
from PyQt5.QtNetwork import QNetworkReply
from PyQt5.QtNetwork import QSslConfiguration
from PyQt5.QtCore import QUrl


 class ForRec(object):
	def Reqest(self,reply):
		print(reply.readAll())
	return None
   

if __name__ == '__main__':

 manager = QNetworkAccessManager
 request = QNetworkRequest 
# reply = QSslConfiguration(QSsl.TlsV1_2

 config = QSslConfiguration

# config = config.defaultConfiguration()
# config.setProtocol(reply)
# request.setSslConfiguration(config.defaultConfiguration())
 request.setUrl(QUrl("https://api.telegram.org/bot182003178:AAFMJGLwIHW4zGBNhwr0hwOXyIkObyP9ZTU/getUpdates"));
 request.setHeader(QNetworkRequest.ServerHeader, "application/json")

 manager.get(request)




