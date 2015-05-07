import httplib2
import pprint
#libraries for gdrive file upload
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow
#libraries for web browsing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#libraries for onedrive file upload

#libraries for dropbox file upload

class file:#bas class file
	authorized=False#whether authorization has taken place or not
	def __init__(self,location):
		self.address=location#address of file on pc
		
	def upload(self):
		pass
	@staticmethod
	def authorize():
		pass

class gdrivefile(file):
	drive_service=None
	def upload(self):
		if gdrivefile.authorized==False :
			gdrivefile.authorize()
			gdrivefile.authorized=True

		FILENAME = self.address
		media_body = MediaFileUpload(FILENAME, mimetype='', resumable=True)
		body = {
		  'title': FILENAME,
		  'description': '',
		  'mimeType': ''
		}

		file = gdrivefile.drive_service.files().insert(body=body, media_body=media_body).execute()
		#pprint.pprint(file)

	@staticmethod
	def authorize():
		CLIENT_ID = '268285193546-qpu3mbasinue8ofpiah50fu928lcf24b.apps.googleusercontent.com'
		CLIENT_SECRET = '0iyrUyCs-MhAIyOMeYKeeQO-'

		# Check https://developers.google.com/drive/scopes for all available scopes
		OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

		# Redirect URI for installed apps
		REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

		flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE,
                           redirect_uri=REDIRECT_URI)
		authorize_url = flow.step1_get_authorize_url()
		#print 'Go to the following link in your browser: ' + authorize_url
		driver=webdriver.Firefox()#depends on your browser
		driver.get(authorize_url)
		code = input('Enter verification code: ').strip()#change here
		credentials = flow.step2_exchange(code)

		# Create an httplib2.Http object and authorize it with our credentials
		http = httplib2.Http()
		http = credentials.authorize(http)

		gdrivefile.drive_service = build('drive', 'v2', http=http)

class odrivefile(file):
	def upload(self):
		#code for upload
		pass

	@staticmethod
	def authorize():
		pass
		#code for authorization	

class drobboxfile(file):
	def upload(self):
		#code for upload
		pass

	@staticmethod
	def authorize():
		pass
		#code for authorization	
add=input('enter address of a file')
f1=gdrivefile(add)
f1.upload()
f1.upload()

