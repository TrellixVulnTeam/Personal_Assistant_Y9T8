import win32com.client as wincl
import win32

def speak(y):
	aspeak = wincl.Dispatch("SAPI.SpVoice")
	aspeak.Speak(y)
 
if __name__ == '__main__':
	speak("hello sir how may i help u")
