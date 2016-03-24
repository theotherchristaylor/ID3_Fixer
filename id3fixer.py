import sys
import os

def main():



    if sys.argv[1] == "":
        print "USAGE: python id3fixer.py <directory of mp3 files>"
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
    
    for song in songList:
        print "---------------------------------------------------------------------"
        print "EDITING"
        print song
        print ""
        artist = str(raw_input("Artist: "))
        title = str(raw_input("Title: "))
        print ""
        executeLine = "id3v2 -D \"" + directory + song + "\""
        os.system(executeLine)
        executeLine = "id3v2 -t \"" + title + "\" -a \"" + artist + "\" \"" + directory + song + "\""  
        os.system(executeLine)
        print "[+] Changed artist to " + artist + " and title to " + title
        newFilename = artist + " - " + title + ".mp3"
        executeLine = "mv \"" + directory + song + "\" \"" + directory + newFilename + "\""
        os.system(executeLine)
        print "[+] Changed filename to " + newFilename
        

    print ""
    print "[+] Editing complete!"

main()
