import requests
class Client():
	def __init__(self):
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
		self.api="https://goo-gl.me/api/v1"
	def get_link(self,url):
		data={"long_url":url,"type":"splash"}
		return requests.post(f"{self.api}/link",headers=self.headers,json=data).json()