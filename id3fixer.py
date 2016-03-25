# id3fixer.py 
# A script to fix ID3 tags of downloaded music
# 
# Written by Chris Taylor, 3/23/16

import sys
import os
from player import Player
import time
import subprocess

def main():

    player = Player()
    #player.play("../House/Julian\ Jeweil\ -\ Mad.mp3")
    #time.sleep(5)
    #player.stop()
    #exit(0)

    if len(sys.argv) < 2:
        print "\nUSAGE: python id3fixer.py <directory of mp3 files>\n"
        exit(0)
    else:
        directory = sys.argv[1]
    
    #user_input = raw_input("Enter the path of your file: ")
    #directory = str(user_input)

    if os.path.isdir(directory):
        print "[+] Path exists."
        fileList = os.listdir(directory);
        songList = []
        for song in fileList:
            if song.endswith("mp3"):
                songList.append(song)
        print "[+] Found " + str(len(songList)) + " songs."
    else:
        print "[-] Path does not exist."
        exit(0)
    
    os.system("clear")
    for song in songList:
        print ""
        print "---------------------------------------------------------"
        print "EDITING"
        print song
        print ""
        if str(raw_input("Press ENTER to edit or N for next song: ")) != 'N':
            track = str(directory + song)
            player.play(track)
            artist = str(raw_input("Artist: "))
            title = str(raw_input("Title: "))
            comments = str(raw_input("Comments: "))
            print ""
            executeLine = "id3v2 -t \"" + title + "\" -a \"" + artist + "\" -c \"" + comments + "\" \"" + directory + song + "\""  
            os.system(executeLine)
            print "[+] Changed artist to " + artist + " and title to " + title
            newFilename = artist + " - " + title + ".mp3"
            executeLine = "mv \"" + directory + song + "\" \"" + directory + newFilename + "\""
            os.system(executeLine)
            print "[+] Changed filename to " + newFilename
            player.stop()
            print ""
            if str(raw_input("Press ENTER for next song, X to quit: ")) == 'X':
                exit(0)
        

    print ""
    print "[+] Editing complete!"

main()
