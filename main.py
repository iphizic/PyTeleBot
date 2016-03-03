from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply, QSslConfiguration, QSsl
from PyQt5.QtCore import QUrl


class ForRec(QNetworkAccessManager):
	def Reqest(self,reply):
		print(reply.readAll())
   

if __name__ == '__main__':

	url = "https://api.telegram.org/bot"

	manager = QNetworkAccessManager()
	request = QNetworkRequest()

	config = QSslConfiguration.defaultConfiguration()
	config.setProtocol(QSsl.SecureProtocols)

	request.setSslConfiguration(config)
	request.setUrl(QUrl(url));
	request.setHeader(QNetworkRequest.ServerHeader, "getUpdates")

	#manager.get(request)




