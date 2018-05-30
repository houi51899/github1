==========================================================================================================
This is a exam project using openjtalk to develop a alarm and share it in Github. (speech synthesis)


The manual consists two parts. In the first part, I will share the experience of developing the alarm with speech synthesis engine. In the second part, I want to share the experience of how to connect Visual Studio Code with Github to manage the version of the project.
Beware that all the opration is done in ubuntu18.04LTS
----------------------------------------------------------------------------------------------------------
Part 1

Preperation for openjtalk coding.
Before the coding, we need to install some SDK. 

1 install the engine (open-jtalk):

$sudo apt-get install open-jtalk open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001

2 download the voice file(zip):

$wget https://sourceforge.net/projects/mmdagent/files/MMDAgent_Example/MMDAgent_Example-1.6/MMDAgent_Example-1.6.zip/download -O MMDAgent_Example-1.6.zip

3 unzip the voice file:

$unzip MMDAgent_Example-1.6.zip MMDAgent_Example-1.6/Voice/*

$sudo cp -r MMDAgent_Example-1.6/Voice/mei/ /usr/share/hts-voice

#with the SDK above you have enough material to build a simple synthesis program.
#As for the code sourse, please check the file "test.py" in the same folder. 


------------------------------------------------------------------------------------------------------------
Part 2

Simple manual for the setup for VScode to Github.

 In the beginning,let's "cd" to get in the directory where the files there you want to upload and update

1. 
$git init
#initiate a git in this folder.

2.
$git remote add origin https://github.com/......../....git
#address this folder to the project in Github(replace the address with your address in github)

 When upload,go into the same 

1.
$git add .  
#select all the files here or use command: $git add "filename" to select  a single file  
#PS.when use "visual studio code"'s git, press the "+"button to add/select the file, and do not! not! not! use the commit button function in VScode )

2.
$git commit -m "comment"  
#commit the selected file(do input this command in console)

3.
$git push origin master  # upload the files to the git

Option
#$git pull origin master #update the current files from your github  

#$git status #confirm the current status

------------------------------------------------------------------
#Acknowledge

I want thank Mr.honma for the help in connecting the VScode to Github 
