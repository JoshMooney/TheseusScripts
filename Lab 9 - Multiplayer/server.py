from tornado import websocket, web, ioloop, httpserver
import tornado, json

userIP = dict()

def sendToAll(msg):
	for key in userIP:
		userIP[key].write_message(msg)

def CheckJoin(self):
	msg=dict()
	if len(userIP.keys()) < 2:
		userIP[self.request.remote_ip] = self
		msg["type"]="Joined"; #set your type here
		if len(userIP.keys())  == 1:
			msg["data"]="WAITING_FOR_PLAYERS";
			msg["ID"] = len(userIP.keys())
			msg=json.dumps(msg)
			self.write_message(msg)
		if len(userIP.keys()) == 2:
			msg["data"]="STARTING_GAME";
			msg["ID"] = len(userIP.keys())
			msg=json.dumps(msg)
			sendToAll(msg)
	else:
		msg["type"]="Join UnsuccessFul - Session Full"
		self.write_message(msg)

def sendToAllButPlayer(self, R):
	for key in userIP:
		if key is not self.request.remote_ip:
			msg=dict()
			msg["type"] = "Touch"
			msg["Pos"] = {"X":R["Pos"]["X"], "Y":R["Pos"]["Y"]}
			msg["IP"] = self.request.remote_ip
			msg=json.dumps(msg)
			userIP[key].write_message(msg)
			print("Message Sent To: " + self.request.remote_ip)

#Extends the tornado websocket handler
class WSHandler(tornado.websocket.WebSocketHandler):
	def check_origin(self,origin):
		return True

	def open(self):
		print("Websocket Opened")
		
	def on_close(self):
		print("Connection Closed")

	def on_message(self, message):
		R = json.loads(message)
		if R['request'] == 'join':
			CheckJoin(self)
		if R['request'] == "Touch":
			sendToAllButPlayer(self, R)

app = tornado.web.Application([
	(r'/test', WSHandler),
	])

if __name__ == '__main__':
	#what is 8080 ?
	app.listen(4040)
	tornado.ioloop.IOLoop.instance().start()
