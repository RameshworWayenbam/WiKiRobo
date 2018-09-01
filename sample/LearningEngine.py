import ConversationEngine
import SpeakingEngine
import ListeningEngine
lang='en'

def LNow():
	# question 
	lrq = ConversationEngine.ai("lrq")
	SpeakingEngine.tts(lrq,lang)
	rsq = ListeningEngine.listener()
	# answer 
	lra = ConversationEngine.ai("lra")
	SpeakingEngine.tts(lra,lang)
	rsa = ListeningEngine.listener()
	tob = "\n"+rsq+'='+rsa
	ToBrain(tob)
	# thanks
	ltq = ConversationEngine.ai("ltq")
	SpeakingEngine.tts(ltq,lang)	

def ToBrain(text):
	f = open("brain.br", "a")
	f.write(text)
def main():
	LNow();
if __name__ == "__main__":
    main()		