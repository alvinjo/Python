import os
from pygame import mixer
import time


mixer.init()
musicPath = "/home/pi/music/"
songList = []
songNum = 1


def getNames():

    directory = os.fsencode(musicPath)
    for filename in os.listdir(directory):
        song = filename.decode("utf-8")
        print(song)
        songList.append(musicPath+song)


def queue():
    global songNum
    print("queue called")
    #pos = mixer.music.get_pos()
    try:
        print("try")
        while (songNum < len(songList)):
            time.sleep(2)
            #print("while")
            if (int(mixer.music.get_pos()) == -1):
                #print("pos -1")
                print("playing next song")
                mixer.music.load(songList[songNum])
                songNum += 1
                mixer.music.play()

    except KeyboardInterrupt:
        mixer.music.stop()

        


def playSong():
    mixer.music.load(songList[0])
    mixer.music.play()
    queue()
    

    
getNames()
playSong()
