import getpass, imaplib

class Mailctl:
	"""Interface to send/receive mail commands"""

	def __init__(self):
		self.imap = None

	def connect(self, server):
		print('Connecting to ', server, '...', sep='')
		try:
			self.imap = imaplib.IMAP4_SSL(server)
		except(imaplib.IMAP4.error):
			return 'Connection failure'

		return 'Connected'

	def login(self, email, password):
		if (self.imap == None):
			raise(NoConnection('No connection'))
		self.imap.login(email, password)

	def fetchMail():
		pass

	def sendMail():
		pass

	class NoConnection(Exception):
		def __init__(self, value):
			self.value = value
		def __str__(self):
			return repr(self.value)


if (__name__ == '__main__'):
	mail = Mailctl()

	mail.connect('imap.gmail.com')

	while (True):
		try:
			mail.login(input('Email: '), getpass.getpass())
		except (imaplib.IMAP4.error):
			print('Login failed')
			continue

		break

	print ('Logged in!')
