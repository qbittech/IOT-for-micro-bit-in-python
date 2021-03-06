from microbit import uart, sleep

class IOT:
    ipadress = "0.0.0.0"
    BotApiKey = "yourBotApiKey"
    MyChannelName = "yourChannelName"

    def __readUntil(self, uartObject, termination):
	result = ''
	while True:
	   if uartObject.any():
	      byte = uartObject.read(1)
	      result = result + chr(byte[0])
	      if chr(byte[0]) == termination:
	      break
	      sleep(100)
	return result

    def connect_wifi(self, yourSSID,yourPASSWORD):
	#connect to WIFI
	uart.init(baudrate=9600, tx = pin0, rx = pin1)
	uart.write("\r")
	self.__readUntil(uart, '\r')
	uart.write("|2|1|", yourSSID, ",", yourPASSWORD, "|\r")
	self.__readUntil(uart, '3')
	ipadress = self.__readUntil(uart, '\r')
	uart.init(baudrate=115200)
	print(ipadress)
        return True

    def connect_iot_cloud(self, server,port,user,password):
	#connect to MQTT Broker server
	'''Thingspeak; server="api.thingspeak.com";port="80"
	   Blynk; server="blynk-cloud.com" ;http port="8080"; https port="9443"
	exemple:
	'''
	uart.write("\r")
	self.__readUntil(uart, '\r')
	uart.write("|4|1|1|", server,"|", port, "|", user, "|", password, "|\r")
	self.__readUntil(uart, '4')
	self.__readUntil(uart, '1')
	self.__readUntil(uart, '1')
	self.__readUntil(uart, '1')
	return True

    def subscribe(self, topicName):
	#subscribe on topic
	uart.write("\r")
	self.__readUntil(uart, '\r')
	uart.write("|4|1|2|", topicName, "|\r")
	self.__readUntil(uart, '4')
	self.__readUntil(uart, '1')
	self.__readUntil(uart, '2')
	self.__readUntil(uart, '1')
	return True

    def publish(self, topicName, message):
	#publish a message to Broker on topic
	uart.write("\r")
	__readUntil(uart, '\r')
	uart.write("|4|1|3|", topicName, "|", message, "|\r")
	self.__readUntil(uart, '4')
	self.__readUntil(uart, '1')
	self.__readUntil(uart, '3')
	self.__readUntil(uart, '1')
	return True

    def send_telegram(self, BotApiKey, MyChannelName, message):
	#publish a message to Bot on telegram
	uart.write("\r")
	self.__readUntil(uart, '\r')
	uart.write("|3|1|https://api.telegram.org/bot", BotApiKey, "/sendMessage?chat_id=",MyChannelName,"&text=" message, "\r")
	self.__readUntil(uart, '3')
        result = self.__readUntil(uart, '\r')
	return True
