import sys, getpass, imaplib, email

class Mailctl:
	"""Interface to send/receive mail commands"""

	def __init__(self):
		self.imap = None
		self.boxes = {}

	def connect(self, server):
		print('Connecting to ', server, '...', sep='')
		try:
			self.imap = imaplib.IMAP4_SSL(server)
		except(imaplib.IMAP4.error):
			return 'Could not connect'

		return 'Connected'

	def login(self, email, password):
		if (self.imap == None):
			raise(NoConnection('No connection'))

		try:
			self.imap.login(email, password)
		except(imaplib.IMAP4.error):
			raise(LoginFailure)

	def fetchBox(self, box):
		print('Fetching ', box, '...', sep='')
		self.imap.select(box, 1)

		result, data = mail.imap.search(None, "ALL")
		ids = data[0].split()

		messages = []
		for id in ids:
			result, data = self.imap.fetch(id, "(RFC822)")
			raw_email = data[0][1].decode('utf-8')
			messages.append(email.message_from_string(raw_email))

		self.boxes[box] = messages

	def getMessage(self, box, messageNum):
		return self.boxes[box][messageNum]

	def showMessage(self, box, messageNum, part=''):
		"""Shows the specified part of a message from a particular mailbox.
			box - mailbox/folder the message is in
			messageNum - sequence number of the message
			part - which part of the message, i.e. subject, text, etc.
				Defaults to '', which means all."""

		if (part == ''):
			print(self.boxes[box][messageNum])
		else:
			print(self.boxes[box][messageNum][part])


	def sendMail(self):
		pass

	def close(self):
		self.imap.logout()


	class NoConnection(Exception):
		def __init__(self, value):
			self.value = value
		def __str__(self):
			return repr(self.value)

	class LoginFailure(Exception):
		def __init__(self, value):
			self.value = value
		def __str__(self):
			return repr(self.value)

if (__name__ == '__main__'):
	mail = Mailctl()

	mail.connect('imap.gmail.com')
	try:
		mail.login('zjmichen@gmail.com', 'hrbaoxuiwvlmsmdc')
	except (imaplib.IMAP4.error):
		print('Login failed')
		sys.exit()


	print ('Logged in!')

	mail.fetchBox('INBOX')

	# mail.showMessage('INBOX', 0, 'text')
	m = mail.getMessage('INBOX', 1)
	print (m.get('Subject'))

	mail.close()