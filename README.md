# ID3 Fixer
Python program to "Fix" ID3 tags of downloaded mp3 files. 

## Usage
python id3fixer.py <path to mp3 files>

## Actions
id3fixer will find all mp3 files in the directory given on the command line. For each mp3 file, it will:
1. Ask you what you believe to be the actual artist and title of the file
2. Delete the existing ID3 tags
3. Create a new ID3 tag with the artist and title that you specified, leaving every other value empty
4. Change the filename of the mp3 to "<artist> - <title>" using the artist and title you specified. 
