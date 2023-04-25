from gtts import gTTS
import os
import time
from pygame import mixer
mixer.init()
#cant repeat error(Put on every case ending
#while(mixer.music.get_busy()):
    #time.sleep(1)
#mixer.music.unload()

#importable
#TTstudnm
#TTstr
#playsn
#TTstudnomask

def TTstudnm(student_name):
    mixer.music.unload()
    mixer.init()
    mytext = "".join(["Student ID Scanned..",student_name])
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("audio/studid.mp3")
    mixer.music.load("audio/studid.mp3")
    mixer.music.set_volume(1.0)
    mixer.music.play()

def TTstr(string):
    mixer.music.unload()
    mixer.init()
    language = 'en'
    myobj = gTTS(text=string, lang=language, slow=False)
    myobj.save("audio/str.mp3")
    mixer.music.load("audio/str.mp3")
    mixer.music.set_volume(1.0)
    mixer.music.play()

def playsn(name):
    mixer.music.unload()
    mixer.init()
    soundfile = "".join(["audio/",name,".mp3"])
    mixer.music.load(soundfile)
    mixer.music.set_volume(1.0)
    mixer.music.play()

def TTstudnomask(student_name):
    mixer.music.unload()
    mixer.init()
    mytext = "".join(["No Mask Detected on ",student_name])
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("audio/studnomask.mp3")
    mixer.music.load("audio/studnomask.mp3")
    mixer.music.set_volume(1.0)
    mixer.music.play()


def main():
    pass

if __name__ == "__main__":
    main()