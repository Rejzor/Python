import imaplib,subprocess
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('damian.kuter@gmail.com','yeczpzjgalqidymv')
typ, data = mail.select('INBOX')
typ, data = mail.search(None, 'ALL')
all_mails=[]
for num in data[0].split():
	all_mails.append(num)
typ, data = mail.fetch(all_mails[-1], '(RFC822.SIZE BODY[HEADER.FIELDS (SUBJECT)])')#Temat ostatniej
message_last = data[0][1]
typ1, data1 = mail.fetch(all_mails[-2], '(RFC822.SIZE BODY[HEADER.FIELDS (SUBJECT)])')#Temat ostatniej
message_last1 = data1[0][1]
typ, data = mail.search(None, '(UNSEEN)')#Ile nieodczytanych ogolnie
unseen_messages = len(data[0].split())
mail.logout()
notify=("\n\nNieodczytane: {}\n\nTemat ostatniej: {}Temat przedostatniej: {}").format(unseen_messages,message_last[8:],message_last1[8:])#,message_before_last[8:])
subprocess.Popen(['notify-send', notify])
