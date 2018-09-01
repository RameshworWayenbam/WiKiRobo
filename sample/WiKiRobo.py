import ListeningEngine
import SpeakingEngine
import ConversationEngine
import LearningEngine
import Issue

def robo():
	try:
		lang = 'en'
		txx =''
		wel = ConversationEngine.ai("wel")
		SpeakingEngine.tts(wel,lang)
		while True:
			try:
				text = ListeningEngine.listener()
				if text=='learning mode':
					LearningEngine.LNow()
				elif text=='create issue':
					Issue.Create()
				elif text=='issue summary':
					Issue.Summary()
				else:
					txx = text
					SpeakingEngine.nerves(text, lang)

			except Exception as e:
				sye = ConversationEngine.ai("sye")
				SpeakingEngine.tts(sye,lang)
				raise
			else:
				pass
			finally:
				pass

			if txx =='bye':
				tqn = ConversationEngine.ai("tqn")
				SpeakingEngine.tts(tqn,lang)
				break 				
	except Exception as e:
		print("Opps! Sorry.......!")
		pass
	else:
		pass
	finally:
		pass
def main():
	robo();
if __name__ == "__main__":
    main()	