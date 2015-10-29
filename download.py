import urllib

class Downloader():
	def __init__(self,url):
			self.url = url
			self.contents= ''
	def download(self):
		browswer=urllib.urlopen(self.url)
		response=browswer.getcode()
		if response == 200:
			self.contents = browswer.read()