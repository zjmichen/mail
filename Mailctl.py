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
			# mail.login(input('Email: '), getpass.getpass())
			mail.login('zjmichen@gmail.com', 'hrbaoxuiwvlmsmdc')
		except (imaplib.IMAP4.error):
			print('Login failed')
			continue

		break

	print ('Logged in!')

	# print(mail.imap.list()[1][0])

	for box in mail.imap.list()[1]:
		print(box)

	mail.imap.select('INBOX')
	result, data = mail.imap.search(None, "ALL")
	ids = data[0]
	id_list = ids.split()

	latest_id = id_list[-1]

	result, data = mail.imap.fetch(latest_id, "(RFC822)")

	raw_email = data[0][1]
	print(raw_email)