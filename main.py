import pypandoc
# uncomment line 3-4 if pypandoc or pandoc is not found
from pypandoc.pandoc_download import download_pandoc
download_pandoc()

import pyttsx3
# in case of libspeak.so.1 error install: pip install pyaudio
# if can't build pyaudio install: espeak and libespeak-dev (portaudio19-dev also might make it build)
# these are for tts audio styles

# tts = text to speech
# tts initialization
engine = pyttsx3.init()
newVoiceRate = 110
engine.setProperty('rate', newVoiceRate)

# tts from user input
speak = input("Enter text to speak: ")
engine.say(speak)
engine.runAndWait()

# export docx or any file into text file to read in next step
document = 'java.docx'
output = pypandoc.convert_file(document, 'plain', outputfile="converted_text.txt")
assert output == ""

# Read from txt file
with open('converted_text.txt', 'r') as f:
    textfile_content = f.readlines()
    textfile_content = [x.replace('\n', '') for x in textfile_content]
    # print(textfile_content)

engine.say(textfile_content)
engine.runAndWait()
