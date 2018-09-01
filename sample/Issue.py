import cx_Oracle
import ListeningEngine
import SpeakingEngine

lang ='en'
def dbConnect():
				con = cx_Oracle.connect('user/password@localhost:1521/orcl')
				return con

def intgration(txt):
	cn = dbConnect()
	cu = cn.cursor()

	title = txt

	try:
  		cu.callproc('proc_issue_creation',[title]) #title is parameter
	except cx_Oracle.DatabaseError as exception:
  		print ('Failed to call procedure\n')
  		exit (1)
	cu.close()
	cn.close()

def summary_():
	cn = dbConnect()
	cu = cn.cursor()

	try:
  		tx = cu.callfunc('fn',cx_Oracle.STRING,['1']) #passing single parameter
  		return tx
	except cx_Oracle.DatabaseError as exception:
  		print ('Failed to call function\n')
  		raise
  		exit (1)
	cu.close()
	cn.close()


def Create():
	tx="what is the issue title"
	SpeakingEngine.tts(tx,lang)
	issueTitle = ListeningEngine.listener()
	intgration(issueTitle)
	tx="Issue created, thank you"
	SpeakingEngine.tts(tx,lang)

def Summary():
	tx=summary_()
	SpeakingEngine.tts(tx,lang)

def IssueAPI(tx):
	if tx=="issue create":
		Create()
	elif tx=="issue summary":
		Summary()
	else:
		pass

def main():
	#tx = getText()
	#print(tx)
	#intgration('Hello Hello')
	#intgration(tx)
	tx = summary_()
	print(tx)
if __name__ == "__main__":
    main()
